DBNAME=tp1 # nom de la base de données à sauvegarder

mysqldump $DBNAME -uroot -p$MYSQL_ROOT_PASSWORD > dump/$DBNAME.sql