<?php
	include('utente.php');
	session_start();

	$nickname = "";
	$email    = "";
	$errors = array(); 
	$_SESSION['success'] = "";
	
	//!NOTE  ─── CONNESSIONE AL DATABASE ────────────────────────────────────────────────────
	//$db = mysqli_connect('localhost', 'root', '', 'wiki_test');

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		/* Ricevi dati dal form
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$password_1 = mysqli_real_escape_string($db, $_POST['password_1']);
		$password_2 = mysqli_real_escape_string($db, $_POST['password_2']);
		*/
		$nickname = $_POST['nickname'];
		$email = $_POST['email'];
		$naz = $_POST['naz'];
		$dataNascita = $_POST['dataN'];
		$password_1 = $_POST['password_1'];
		$password_2 = $_POST['password_2'];

		// Controlla la compilazione del form
		if (empty($nickname)) { array_push($errors, "Nickname necessario"); }
		if (empty($email)) { array_push($errors, "Email necessaria"); }
		if (empty($naz)) { array_push($errors, "Nazionalità necessaria"); }
		if (empty($dataNascita)) { array_push($errors, "Data di nascita necessaria"); }
		if (empty($password_1)) { array_push($errors, "Password necessaria"); }

		if ($password_1 != $password_2) {
			array_push($errors, "Le password non sono uguali");
		}

		// Registra l'utente solo se non ci sono errori
		if (count($errors) == 0) {
			$password = md5($password_1);//Cripta la password
			/*$query = "INSERT INTO db_users (password, mail, user_login) 
					  VALUES('$password','$email','$username')";
			mysqli_query($db, $query);*/

			if (!isset($_SESSION['utenti'])){
				$_SESSION['utenti'] = array(new Utente($nickname, $email, $naz, $dataNascita, $password));
				array_push($errors, "Registrazione effettuata!");
				$_SESSION['nickname'] = $nickname;
				$_SESSION['success'] = "Hai eseguito il login";
				sleep(3);
				header('location: ../index.php');
			}else{
				$arrayUtenti = $_SESSION['utenti'];
				$flag = FALSE;
				foreach($arrayUtenti as $user){
					if($user->getNickname() == $nickname){
							$flag = TRUE;
					}
				}
				if(!$flag){
					array_push($arrayUtenti, new Utente($nickname, $email, $naz, $dataNascita, $password));
					$_SESSION['nickname'] = $nickname;
					$_SESSION['success'] = "Hai eseguito il login";
					header('location: ../index.php');
				}else{
					array_push($errors, "Nickname già esistente!");
				}
			}
		}

	}

	// LOGIN USER
	if (isset($_POST['login_user'])) {
		/*$username = mysqli_real_escape_string($db, $_POST['username']);
		$password = mysqli_real_escape_string($db, $_POST['password']);*/
		$nickname = $_POST['nickname'];
		$password = $_POST['password'];

		if (empty($nickname)) {
			array_push($errors, "Username necessaria");
		}
		if (empty($password)) {
			array_push($errors, "Password necessaria");
		}

		if (count($errors) == 0) {
			$password = md5($password);
			/*$query = "SELECT * FROM db_users WHERE user_login='$username' AND password='$password'";
			$results = mysqli_query($db, $query);

			if (mysqli_num_rows($results) == 1) {
				$_SESSION['username'] = $username;
				$_SESSION['success'] = "Hai eseguito il login";
				header('location: ../pages/logged.html');
				//
			}else {
				array_push($errors, "Errata username/password combinazione");
			}*/
			if (!isset($_SESSION['utenti'])){
				array_push($errors, "Nessun utente presente nel DB");
			}else{
				$arrayUtenti = $_SESSION['utenti'];
				$flag = FALSE;
				foreach($arrayUtenti as $user){
					array_push($errors, $user->getNickname());
					if($user->getNickname() == $nickname){
						if($user->getPasw() == $password){
							$flag = TRUE;
							$_SESSION['nickname'] = $nickname;
							$_SESSION['success'] = "Hai eseguito il login";
						}
					}
				}
				if(!$flag){
					array_push($errors, "Nickname eo password errati!");
				}else{
					array_push($errors, "Hai eseguito il login");
					sleep(2);
					header('location: ../index.php');
				}
			}
		}
	}

?>