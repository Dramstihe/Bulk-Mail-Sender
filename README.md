<h1>Bulk Email Sender</h1>
<p>This script allows you to easily send bulk emails using the <code>smtplib</code> library and <code>email.mime.text</code> module in Python. Simply add the email addresses to the <code>emails.txt</code> file, and a message in the <code>message.txt</code> file, and the script will handle the rest!</p>
<p>It also includes a feature to check for valid email addresses, and removes any invalid addresses from the list before sending.</p>
<p>In case of any errors while sending an email, the script will wait for 5 minutes before continuing, to avoid hitting the email server's sending limit.</p>
<p>It also writes the list of remaining valid emails after sending the emails to the file. </p>
<h2>Features:</h2>
<ul>
<li>Bulk email sending</li>
<li>Check for valid email addresses</li>
<li>Error handling and waiting before continuing</li>
<li>Write the list of remaining valid emails to the file</li>
</ul>
<h2>Usage:</h2>
<ol>
<li>Add email addresses to <code>emails.txt</code> file</li>
<li>Add your message to <code>message.txt</code> file</li>
<li>Run the script</li>
</ol>
<p>Note: You need to use your own email id and password for sending the emails</p>
<h2> 🚀 Give it a try!</h2>
<h2> 💻 Perfect for automating your email campaigns!</h2>
</br>
<b>Note:</b> This script uses gmail smtp server, if you want to use other servers you need to change the server settings accordingly.
