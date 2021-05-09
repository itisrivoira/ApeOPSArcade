<?php
	include('utente.php');
	include('connection.php');
	session_start();

	$nickname = "";
	$email    = "";
	$errors = array(); 
	$_SESSION['success'] = "";
	
	//!NOTE  ─── CONNESSIONE AL DATABASE ────────────────────────────────────────────────────
	$mysqli = $con;

	if (isset($_GET['change'])) {
		if(isset($_GET['salva'])){
			$newNickname = $mysqli->real_escape_string($_POST['nickname']);
			$newEmail = $mysqli->real_escape_string($_POST['email']);
			$newNaz = $mysqli->real_escape_string($_POST['naz']);
			$newDataNascita = $mysqli->real_escape_string($_POST['dataN']);
			$newPassword_1 = $mysqli->real_escape_string($_POST['password_1']);
			$newPassword_2 = $mysqli->real_escape_string($_POST['password_2']);

			if (strlen($newNickname) > 25) { array_push($errors, "Nickname scelto troppo lungo"); }
			if (DateTime::createFromFormat('Y-m-d', $newDataNascita) === false) { array_push($errors, "Data scelta non disponibile, riprovare"); }

			if (strlen($newPassword_1) < 6) {
				array_push($errors, "La password è troppo debole");
			}

			if ($newPassword_1 != $newPassword_2) {
				array_push($errors, "Le password non sono uguali");
			}

			if($newNickname != $_SESSION['nickname']){
				// Controllo che non esista un utente con nick identico
				$query = "SELECT * FROM utente 
				WHERE utente.Nickname = '$nickname';";
				$results = $mysqli->query($query);

				if (!$results) {
					array_push($errors, "Error description: " . $mysqli -> error);
				}

				if ($results->num_rows == 1) {
					array_push($errors, "Nickname già in uso!");
				}
			}

			if($newEmail != $_SESSION['nickname']){
			$query = "SELECT * FROM utente 
			WHERE utente.Email = '$email';";
			$results = $mysqli->query($query);

			if (!$results) {
				array_push($errors, "Error description: " . $mysqli -> error);
			}

			if ($results->num_rows == 1) {
				array_push($errors, "Email già in uso!");
			}
		}else{
			$nickname = $_SESSION["nickname"];
			$query = "SELECT * FROM utente
			WHERE utente.Nickname = '$nickname';";
			$results = $mysqli->query($query);

			if ($results->num_rows == 1) {
				$row = $results->fetch_array(MYSQLI_ASSOC);
				$nicknameResult = $row["Nickname"];
				$emailResult = $row["Email"];
				$nazResult = $row["Nazione"];
				$dataResult = $row["DataNascita"];
			}else {
				array_push($errors, "Errore durante il recupero dei dati");
			}
		}
	}

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		//Ricevi dati dal form
		$nickname = $mysqli->real_escape_string($_POST['nickname']);
		$email = $mysqli->real_escape_string($_POST['email']);
		$naz = $mysqli->real_escape_string($_POST['naz']);
		$dataNascita = $mysqli->real_escape_string($_POST['dataN']);
		$password_1 = $mysqli->real_escape_string($_POST['password_1']);
		$password_2 = $mysqli->real_escape_string($_POST['password_2']);
		/*$nickname = $_POST['nickname'];
		$email = $_POST['email'];
		$naz = $_POST['naz'];
		$dataNascita = $_POST['dataN'];
		$password_1 = $_POST['password_1'];
		$password_2 = $_POST['password_2'];*/

		// Controlla la compilazione del form
		if (empty($nickname)) { array_push($errors, "Nickname necessario"); }
		if (empty($email)) { array_push($errors, "Email necessaria"); }
		if (empty($naz)) { array_push($errors, "Nazionalità necessaria"); }
		if (empty($dataNascita)) { array_push($errors, "Data di nascita necessaria"); }
		if (empty($password_1)) { array_push($errors, "Password necessaria"); }

		if (strlen($nickname) > 25) { array_push($errors, "Nickname scelto troppo lungo"); }
		if (DateTime::createFromFormat('Y-m-d', $dataNascita) === false) { array_push($errors, "Data scelta non disponibile, riprovare"); }

		if (strlen($password_1) < 6) {
			array_push($errors, "La password è troppo debole");
		}

		if ($password_1 != $password_2) {
			array_push($errors, "Le password non sono uguali");
		}

		
		// Controllo che non esista un utente con nick o email identiche
		$query = "SELECT * FROM utente 
		WHERE utente.Nickname = '$nickname';";
		$results = $mysqli->query($query);

		if (!$results) {
			array_push($errors, "Error description: " . $mysqli -> error);
		}

		if ($results->num_rows == 1) {
			array_push($errors, "Nickname già in uso!");
		}

		$query = "SELECT * FROM utente 
		WHERE utente.Email = '$email';";
		$results = $mysqli->query($query);

		if (!$results) {
			array_push($errors, "Error description: " . $mysqli -> error);
		}

		if ($results->num_rows == 1) {
			array_push($errors, "Email già in uso!");
		}

		// Registra l'utente solo se non ci sono errori
		if (count($errors) == 0) {
			$password = md5($password_1);//Cripta la password
			$query = "INSERT INTO utente VALUES('$nickname','$password','$email','$naz','$dataNascita');";
			$results = $mysqli->query($query);

			if (!$results) {
				array_push($errors, "Error description: " . $mysqli -> error);
			}

			//var_dump($results);

			if ($results) {
				$_SESSION['nickname'] = $nickname;
				$_SESSION['success'] = "Hai eseguito il login";
				array_push($errors, "Hai eseguito il login");
				sleep(2);
				header('location: ../index.php');
			}else {
				array_push($errors, "Errore durante la registrazione, riprovare");
			}
		}

	}

	// LOGIN USER
	if (isset($_POST['login_user'])) {
		$nickname = $mysqli->real_escape_string($_POST['nickname']);
		$password = $mysqli->real_escape_string($_POST['password']);

		if (empty($nickname)) {
			array_push($errors, "Username necessaria");
		}
		if (empty($password)) {
			array_push($errors, "Password necessaria");
		}

		if (count($errors) == 0) {
			$password = md5($password);
			$query = "SELECT utente.Nickname FROM utente
			WHERE utente.Nickname = '$nickname' AND utente.Password = '$password';";
			$results = $mysqli->query($query);

			if ($results->num_rows == 1) {
				$row = $results->fetch_array(MYSQLI_ASSOC);
				$_SESSION['nickname'] = $row["Nickname"];
				$_SESSION['success'] = "Hai eseguito il login";
				array_push($errors, "Hai eseguito il login");
				sleep(2);
				header('location: ../index.php');
			}else {
				array_push($errors, "Nickname eo password errati!");
			}
		}
	}

?>