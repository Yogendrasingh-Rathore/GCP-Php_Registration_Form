1. Create a compute VM using Deployment Manager
	- Create a compute.yaml file
		- The yaml file has all the configuration required
		- Add natIP in accessConfigs in networkInterfaces ... i.e(networkInterfaces -> accessConfigs -> natIP)
		- In this way, we can specify the specific External Ip to that VM Instance
		- Startup Script:
			- sudo apt-get update
			- sudo apt-get install mysql-client -y
			- sudo apt update
			- sudo apt install -y apache2 apache2-utils
			- sudo systemctl start apache2
			- sudo systemctl enable apache2
			- sudo apt install curl
			- sudo chown www-data:www-data /var/www/html/ -R
			- sudo apt-get -y -qq install git
			- cd /var/www/html/
			- sudo rm index.html
			- sudo git clone https://github.com/Yogendrasingh-Rathore/Php-Registartion-Form.git
	- gcloud deployment-manager deployments create my-vm-instance --config=compute.yaml
2. Create a SQL Instance using Deployment Manager
	- Create a vm-sql.yaml file
		- The yaml file has all the configuration required (Location, Type, Size, Users, Password)
		- Add the ipConfiguration in settings to add the Specify Ip Address ... i.e(External IP of that VM)
	- gcloud deployment-manager deployments create my-SQL-instance --config=vm-sql.yaml
3. Create a Database "registration" and a "User" Table on the SQL Instance from the Compute VM
	- mysql -h ExternalIP_of_SQLInstance -u root -p (You will pe prompted for Passport, Enter Password)
		- create database registration;
		- use registration;
		- CREATE TABLE `users` (
					  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
					  `username` varchar(100) NOT NULL,
					  `email` varchar(100) NOT NULL,
					  `password` varchar(100) NOT NULL
					) ENGINE=InnoDB DEFAULT CHARSET=latin1;
4. Allow Firewall rule ingress, so that the VM Instance can be accessed from host machine or some other machines
5. Paste the External IP of that VM Instance on your host machine or the machine that has an access to that VM
