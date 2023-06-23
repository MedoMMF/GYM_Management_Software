import tkinter as tk
import smtplib

class EmailSender:
    def __init__(self, master):
        self.master = master
        master.geometry('795x550+480+200')
        master.iconbitmap('pohots\Silvster gym.ico.ico')
        master.title("Send Email")

        # Create the input fields
        recipient_label = tk.Label(master, text="Recipient:",font=("arial",12,"bold"))
        recipient_label.pack()
        self.recipient_entry = tk.Entry(master,font=("arial",12,"bold"))
        self.recipient_entry.pack()

        subject_label = tk.Label(master, text="Subject:",font=("arial",12,"bold"))
        subject_label.pack()
        self.subject_entry = tk.Entry(master,font=("arial",12,"bold"))
        self.subject_entry.pack()

        body_label = tk.Label(master, text="Body:",font=("arial",12,"bold"))
        body_label.pack()
        self.body_text = tk.Text(master,font=("arial",12,"bold"),height=18)
        self.body_text.pack()

        # Create the send button
        send_button = tk.Button(master, text="Send", command=self.send_email,font=("arial",12,"bold"))
        send_button.pack()

        # Create the success label
        self.success_label = tk.Label(master, text="")
        self.success_label.pack()

    def send_email(self):
        # Get the values from the input fields
        recipient = self.recipient_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END)

        # Create the email message
        message = f"Subject: {subject}\n\n{body}"

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            # Start the TLS encryption
            smtp.starttls()

            # Login to the SMTP server
            smtp.login("email", "email code")

            # Send the email
            smtp.sendmail("email", recipient, message)

        # Show a success message
        self.success_label.config(text="Email sent successfully!")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    email_sender = EmailSender(root)
    root.mainloop()