# flask_4_databases_mysql_vm
504 WK 4 Assignment using MySQL on an Azure VM

## GCP VM Settings:

1. Region: us-central1
2. Machine Config: E2-small
3. Firewall: Allow HTTP/HTTPS traffic

Everything else default

## Azure VM Settings:

1. Security Type: Standard
2. Image: Ubuntu Server 20.04 LTS - x64 Gen2
3. Size: B1ms
4. Create username/password
5. Ports: HTTP/HTTPS/SSH
6. Create new virtual network 
7. Select delete public IP and NIC when VM is deleted

After creation:

1. Open port 3306 with unique priority

## Connect to VM:

1. Connect to VM: $ ssh <username>@<ip address of vm>
2. Update ubuntu server $sudo apt-get update
3. Install MySQL: $ sudo apt install mysql-client mysql-server
4. Create users to connect with: CREATE USER '<new username>'@'%' IDENTIFIED BY '<new password>'
5. Grant privileges to new user: GRANT ALL PRIVILEGES ON *.* TO '<username>'@'%' WITH GRANT OPTION
6. Enter config to allow external connections on port 3306: $ sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
7. Change bind-address and mysqlx-bind-address to 0.0.0.0
8. Restart mysql: $ /etc/init.d/mysql restart

## Database

The database used has two tables: patient and patient_medication. Patient tracks some basic info about the patient with a patient ID number being the primary key. Patient_medicaition tracks individual medications given to patients, linked by the patient_id primary key.

## Errors

The only errors that slowed my process were small syntax errors. I had difficulty loading in my env values but I forgot to include the load_dotenv() function. When loading the MySQL data into an html table, I got a syntax error in my {% for patient in data_1 %} line, but I originally did not include the second %, resulting in the syntax error.


