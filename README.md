# AegisCloud – Automated Malware Scanning in AWS with Lambda & YARA

AegisCloud is a cloud-native, serverless malware detection solution built on AWS Lambda that automates malware scanning and quarantining for files uploaded to Amazon S3. Leveraging custom YARA rules, AegisCloud inspects every S3 file upload in real time, immediately isolating matched threats to a secure quarantine bucket. The project is ideal for cloud security research, DevSecOps pipelines, and compliance use-cases.

---

## 🚀 Features

- **AWS Lambda serverless architecture** — no servers to manage, auto-scales with usage.
- **YARA-powered scanning** — easily extend detection for any file types or threats.
- **Automatic quarantine** — detected threats are moved instantly to a secure S3 bucket.
- **Modular workflow** — add SNS/email notifications or DynamoDB logging in minutes.
- **Easy deployment** — just upload your code, configure S3 triggers, and go.
- **Sample YARA rules & test file instructions provided.**

---

## 🛠️ Tech Stack

- **AWS Lambda (Python)**
- **Amazon S3**
- **YARA** (using Python package and Lambda Layer)
- (Optional: AWS SNS, DynamoDB, Slack, other integrations)

---

## ⚡ Getting Started

### 1. **Clone or Fork this repository**
git clone https://github.com/manivardhan7/AGIES-CLOUD-.git
cd AGIES-CLOUD-



### 2. **Deploy to AWS Lambda**
- Create a new AWS Lambda function (Python 3.9+ recommended).
- Upload `app.py` and any dependencies/layers (YARA).
- Configure your Lambda with S3 event triggers for your **uploads** bucket.

### 3. **Configure your S3 buckets**
- **aegiscloud-threat-uploads:** For incoming files.
- **aegiscloud-threat-quarantine:** For isolating threats.

### 4. **Add or Edit YARA Rules**
- Update `malicious_rules.yar` (or your preferred rules file).
- Place known signatures (like EICAR) for safe testing.

### 5. **Test the Pipeline**
- Upload a test file (e.g. EICAR string) to the uploads bucket.
- Confirm the file is automatically moved to quarantine if detected.

---

## 🔒 Security & Usage Notes

- **Never use real malware for production testing!** Use industry-standard test files like [EICAR](https://www.eicar.org/download-anti-malware-testfile/).
- Do NOT include credentials, secrets, or sensitive config in your public repo.
- Advanced: Integrate alerts, custom response actions, or logging as needed.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

- **manivardhan7** (https://github.com/manivardhan7)
- Pull requests and feedback are welcome!

---

## 💡 Example Use Cases

- Cloud upload security for SaaS, data storage, or enterprise apps.
- Automated DevOps malware pipeline for continuous file scanning.
- Security research into YARA rule performance and tuning.

---

## 📚 Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [YARA Rule Docs](https://yara.readthedocs.io/en/stable/)
- [EICAR test file](https://www.eicar.org/download-anti-malware-testfile/)

