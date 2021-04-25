<?php
    #accesso al database
    define('DBHOST', 'localhost');
    define('DBUSER', 'root');
    define('DBPASS', '');
    define('DBNAME', 'test');
    $con = new mysqli(DBHOST, DBUSER, DBPASS, DBNAME);

    if ($con->connect_errno)
    {
        $codice = $con->connect_errno;
        $errore = $con->connect_error;
        http_response_code(503);
        die("Errore di connessione: $codice - $errore.");
    }
	$con->set_charset("utf8");
?>