# MYSQL

## Notes

- first create `tyrell_corp` db
- add some fake table and data
- create new user `replica_user`@`%` -> match any host identified by a passwrd -> have to save it

[server 1 Master]

- go to `/etc/mysql/mysql.conf.d/mysqld.cnf` or maybe `/etc/mysql/my.cnf` and set the server_id to (unique integer)
- uncomment the binanry log property
- do not use the bind-address, just comment out this parameter
- save and restart mysql server
- create a copy of the corrent situation of (either the hole mysql or just the data base u want) using `mysqldump`
- send tis masterdump.sql to the slave server

[server 2 Slave]

- go to `/etc/mysql/mysql.conf.d/mysqld.cnf` or maybe `/etc/mysql/my.cnf` and set the server_id to (unique integer)
- set bind-address to 127.0.0.1
- save and restart mysql server
- run: `mysql -uroot -p < masterdump.sql` => that create a copie of the master
- to create the slave :
  `CHANGE MASTER TO MASTER_HOST='master ip', MASTER_USER='replica_user', MASTER_PASSWORD='XXXXXXX';`
- start the slave : `START SLAVE;`

## IMPORTANT NOTE TO CONSIDER

- THE SLAVE WILL REMOTEMY CONNECT OT THE MASTER USING THE USER replica_user and the pass given TO TEST THIS USE :
  `mysql -ureplica_user -hremote_IP_address -p`
- SO IN THE MASTER SERVER ALWAYS ALLOW THE SLAVE TO CONNECT IN THE DEFAULT PORT 3306 => CHECK FIREWALL
  -> `sudo ufw allow from remote_IP_address to any port 3306`
- TO TEST SLAVE TYPE : `show slave status\G;`
- U HAVE TO SEE: ` Slave_IO_Running: Yes Slave_SQL_Running: Yes`
- if Slave_I: NO -> prob with connection to master
- if Slave_SQL: NO -> prob with the slave [check this](https://serverfault.com/questions/872911/slave-sql-running-no-mysql-replication-stopped-working)
  maybe some duplicate slave on the server
