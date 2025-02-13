#  Reverse IP Application - Kubernetes Deployment  

This repository contains a **Reverse IP Application** and a **MySQL database**, deployed on **Kubernetes** using **Helm charts**. The application reverses an IP address and stores the result in a MySQL database.  

---

##  Application Overview  

- **Reverse IP App**: A Python-based API that reverses IP addresses and stores them in a MySQL database.  
- **MySQL Database**: Used for persistent storage of reversed IPs.  
- **Kubernetes Deployment**: Deployed using **Helm charts**, with automatic version updates using **GitHub Actions (CI)**.  

---

##  Prerequisites  

Before deploying the application, ensure the following:  

- **Kubernetes cluster** is running  
- **Helm is installed**  
- **Container runtime**: `containerd`  

###  1. Create a Local Directory for Persistent Storage  

MySQL uses a `hostPath` for persistent storage. Create a directory on the **worker node**:  

```bash
sudo mkdir -p /mnt/data
sudo chmod 777 /mnt/data
```
###  2. CI triggered via Github Action, update Chart appVersion.
```bash
  git add .
  git commit -m "Update application version and configurations"
  git push origin main
```
###  3. Helm deployment process
```bash
  git clone git@github.com:praveshjangra/reverse_ip.git
  cd reverse_ip
  helm install reverse-ip-app helm_chart_app/
```
###  3. Database Details
```bash 
    hostname - mysql
    user - root
    password -  password
