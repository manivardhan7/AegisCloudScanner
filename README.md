# AegisCloudScanner – Automated Malware Scanning in AWS with Lambda & YARA

AegisCloudScanner is a cloud-native, serverless malware detection framework built for AWS Lambda, automating malware scanning and S3 file quarantining using YARA rules. Every file uploaded to your monitored S3 bucket is inspected in real time, and detected threats are instantly isolated in a secure quarantine bucket. This solution is designed for cloud security, DevSecOps pipelines, and compliance-focused workflows.

---

## 🚀 Features

- **Serverless AWS Lambda workflow** — scalable, no server management required.
- **YARA-based threat detection** — extendable to any malware/indicator patterns.
- **Real-time quarantine** — infected files auto-moved to a dedicated S3 bucket.
- **Modular integrations** — easily add email/SNS notifications, logging, or third-party alerts.
- **Simple deployment** — upload the Lambda code, attach your YARA rules, and set the S3 trigger.
- **Sample rules and test instructions included.**

---

## 🛠️ Tech Stack

- **AWS Lambda (Python)**
- **Amazon S3**
- **YARA (with Python bindings and Lambda Layer)**
- (Optional: AWS SNS, DynamoDB, Slack)

---

## ⚡ Getting Started

### 1. **Clone or Fork this repository**
git clone https://github.com/manivardhan7/AegisCloudScanner.git
cd AegisCloudScanner


### 2. **Deploy Lambda Function**
- Create a new AWS Lambda for Python 3.9+.
- Upload `app.py` and dependencies (add YARA as a custom layer).
- Connect to your S3 upload bucket (triggered on object created events).

### 3. **Configure S3 Buckets**
- **aegiscloud-threat-uploads:** receives incoming files.
- **aegiscloud-threat-quarantine:** receives detected threats.

### 4. **Edit/Add YARA Rules**
- Place your threat signatures into `malicious_rules.yar` or your custom rules file.

### 5. **Test Your Pipeline**
- Upload a test file (e.g. EICAR test file) to the uploads bucket.
- If detected, your Lambda function will move it to quarantine.

---

## 🔒 Security & Usage

- For testing, use [EICAR test files](https://www.eicar.org/download-anti-malware-testfile/); never use real malware in production environments.
- Exclude sensitive data (AWS credentials, secrets) from your repo.
- Expand with alerting/logging as needed for your security workflow.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.

---

## 🙋 Author

- **manivardhan7** (https://github.com/manivardhan7)

---

## 💡 Example Use Cases

- Cloud-based malware filtering for SaaS and S3 data lakes.
- Serverless threat response and workflow automation.
- Research platform for YARA rule evaluation and improvement.

---

## 📚 References

- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [YARA Rule Documentation](https://yara.readthedocs.io/en/stable/)
- [EICAR Test File](https://www.eicar.org/download-anti-malware-testfile/)
