![image](https://github.com/user-attachments/assets/1f87dccf-0135-41b2-aec0-e70865574e1e)# Aster

### Aster
Nmap scan shows ports 22,80, 1720, 2000 and 5038 open, in particular `5038/tcp open  asterisk    Asterisk Call Manager 5.0.2` is a remote administration utility for VOIP servers. But I first need a set of valid credentials to access it. The website allows me to download a python script which is already byte-compiled. I decompiled it using a tool called `uncompyle6`, but it seems obfuscated so I asked chatGPT to make it look prettier, and this is the result: <br />

    import pyfiglet

    # Line 1: Render "Hello!!" in ASCII art
    o0OO00 = pyfiglet.figlet_format('Hello!!')
    
    # Line 2: A hex-encoded message
    oO00oOo = '476f6f64206a6f622c2075736572202261646d696e2220746865206f70656e20736f75726365206672616d65776f726b20666f72206275696c64696e6720636f6d6d756e69636174696f6e732c20696e7374616c6c656420696e20746865207365727665722e'
    
    # Line 3: Convert hex to bytes
    OOOo0 = bytes.fromhex(oO00oOo)
    
    # Line 4: Decode as ASCII
    Oooo000o = OOOo0.decode('ASCII')
    
    # Line 5-6: Junk dead code for obfuscation
    if 0:
        i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
    
    # Line 7: Another hex-encoded string
    Oo = '476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21'
    
    # Line 8: Decode second message
    I1Ii11I1Ii1i = bytes.fromhex(Oo)
    Ooo = I1Ii11I1Ii1i.decode('ASCII')
    
    # Line 9: More fake obfuscation code
    if 0:
        iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
    
    # Line 10: Print the figlet banner
    print o0OO00

As you can see, there are two hex-encoded strings. If I decode them I get the following strings: 

    Good job, user "admin" the open source framework for building communications, installed in the server.
    Good job reverser, python is very cool!Good job reverser, python is very cool!Good job reverser, python is very cool!
The only thing I get from this is that there's a valid user called `admin`. After doing some research, I found there's a metasploit module I can use to bruteforce logins on asterix:

    use auxiliary/voip/asterisk_login
    set rhosts 10.10.45.134
    set stop_on_success true
    set username admin
    run
![image](https://github.com/user-attachments/assets/f930761f-bed7-4e43-842c-f9fbf4becb6e)<br />
With this credentials I can interact with the asterisk server using netcat: 
    
    Action: Login
    Username: admin
    Secret: <redacted>
I got stuck here for a long time because after entering the secret I did not press the ‘ENTER’ button 2 times(...).<br />
![image](https://github.com/user-attachments/assets/e47fe79a-0239-4488-9877-dadb244d5a98)<br />
After some research, I find out that after login I can execute asterisk commands, in particular this command retrieves information about a SIP user:<br />
![Screenshot 2025-03-24 093612](https://github.com/user-attachments/assets/05497f73-c2ce-4606-98a4-f6a27755fbec)<br />
With this set of credentials I login into harry's ssh account and get the user flag. Now inside harry's home directory there's a file called `Example_Root.jar`. I unzip it and get a java file already compiled in bytecode, similar concept of the python script already compiled that I saw before. To decompile it, first I download cfr (which is a command line java decompiler) from [this website](https://www.benf.org/other/cfr/), transfer the .class file on my machine and then run `java -jar cfr-0.151.jar Example_Root.class`. And this is the compiled code:

    /*
     * Decompiled with CFR 0.151.
     */
    import java.io.File;
    import java.io.FileWriter;
    import java.io.IOException;
    
    public class Example_Root {
        public static boolean isFileExists(File file) {
            return file.isFile();
        }
    
        public static void main(String[] stringArray) {
            String string = "/tmp/flag.dat";
            File file = new File(string);
            try {
                if (Example_Root.isFileExists(file)) {
                    FileWriter fileWriter = new FileWriter("/home/harry/root.txt");
                    fileWriter.write("my secret <3 baby");
                    fileWriter.close();
                    System.out.println("Successfully wrote to the file.");
                }
            }
            catch (IOException iOException) {
                System.out.println("An error occurred.");
                iOException.printStackTrace();
            }
        }
    }
It's not doing anything interesting really, it just checks for the esistence of a file inside `/tmp/`, and if yes, it creates a file inside harry's home directory with "My secret <3 baby". I keep enumerating the system and find an interesting cronjob:<br />
![image](https://github.com/user-attachments/assets/9addc65f-a06f-42db-a7d7-61e0532332e2)<br />
So since we are provided with a java file called `Example_Root.class`, I suppose this is just an example. Maybe root is running the real java code that would put the root flag inside harry's home directory. So just create a file in `/tmp/` and call it `flag.dat`, then wait a few seconds and the root flag actually appears on harry's home directory!

