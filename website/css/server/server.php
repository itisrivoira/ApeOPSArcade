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
		if(isset($_POST['salva'])){
			$newNickname = $mysqli->real_escape_string($_POST['nickname']);
			$newEmail = $mysqli->real_escape_string($_POST['email']);
			$newNaz = $mysqli->real_escape_string($_POST['naz']);
			$newDataNascita = $mysqli->real_escape_string($_POST['dataN']);
			$newPassword_1 = $mysqli->real_escape_string($_POST['password_1']);
			$newPassword_2 = $mysqli->real_escape_string($_POST['password_2']);

			$nickname = $_SESSION['nickname'];
			$query = "SELECT * FROM utente
			WHERE utente.Nickname = '$nickname';";
			$globalResults = $mysqli->query($query);
			$globalRow = $globalResults->fetch_array(MYSQLI_ASSOC);

			if(!empty($newPassword_1) && md5($newPassword_1) != $globalRow['Password']){
				if (strlen($newPassword_1) < 6) {
					array_push($errors, "La password è troppo debole");
				}
	
				if ($newPassword_1 != $newPassword_2) {
					array_push($errors, "Le password non sono uguali");
				}else{
					$nickname = $_SESSION["nickname"];
					$query = "SELECT * FROM utente
					WHERE utente.Nickname = '$nickname';";
					$results = $mysqli->query($query);

					if ($results->num_rows == 1) {
						$row = $results->fetch_array(MYSQLI_ASSOC);
						$passwordResult = $row["Password"];
						$md5Password = md5($newPassword_1);
						if ($md5Password != $passwordResult) {
							$oldNickname = $row['Nickname'];
							$query = "UPDATE utente SET utente.Password = '$md5Password' WHERE utente.Nickname = '$oldNickname';";
							$results = $mysqli->query($query);
							if(!$results){
								array_push($errors, "Errore durante inserimento informazioni dal db");
							}else{
								array_push($errors, "Password aggiornata!");
							}
						}else{
							array_push($errors, "Utilizza una password diversa da quella vecchia!");
						}
					}else{
						array_push($errors, "Errore durante recupero informazioni dal db");
					}
				}
			}

			if(!empty($newNickname)){
				if (strlen($newNickname) > 25) { 
					array_push($errors, "Nickname scelto troppo lungo"); 
				}elseif(strlen($newNickname) < 4){
					array_push($errors, "Nickname scelto troppo corto"); 
				}else{
					if($newNickname != $_SESSION['nickname']){
						// Controllo che non esista un utente con nick identico
						$query = "SELECT * FROM utente 
						WHERE utente.Nickname = '$newNickname';";
						$results = $mysqli->query($query);

						if (!$results) {
							array_push($errors, "Error description: " . $mysqli -> error);
						}else{
							if ($results->num_rows == 1) {
								array_push($errors, "Nickname già in uso!");
							}else{
								$oldNickname = $_SESSION['nickname'];
								$query = "UPDATE utente SET utente.Nickname = '$newNickname' WHERE utente.Nickname = '$oldNickname';";
								$results = $mysqli->query($query);
								if(!$results){
									array_push($errors, "Errore durante inserimento informazioni nel db [NICKNAME]");
								}else{
									array_push($errors, "Nickname aggiornato!");
									$_SESSION["nickname"] = $newNickname;
								}
							}
						}
					}
				}
			}else{
				array_push($errors, "Campo nickname vuoto!");
			}

			if(!empty($newEmail)){
				$nickname = $_SESSION["nickname"];
				$query = "SELECT utente.Email FROM utente
				WHERE utente.Nickname = '$nickname';";
				$results = $mysqli->query($query);
				$results = $results->fetch_array(MYSQLI_ASSOC);
				if($newEmail != $results['Email']){
					$query = "SELECT * FROM utente 
					WHERE utente.Email = '$newEmail';";
					$results = $mysqli->query($query);
	
					if (!$results) {
						array_push($errors, "Error description: " . $mysqli -> error);
					}else{
						if ($results->num_rows >= 1) {
							array_push($errors, "Email già in uso!");
						}else{
							$query = "UPDATE utente SET utente.Email = '$newEmail' WHERE utente.Nickname = '$nickname';";
							$results = $mysqli->query($query);
							if(!$results){
								array_push($errors, "Errore durante inserimento informazioni nel db [EMAIL]");
							}else{
								array_push($errors, "Email aggiornata!");
							}
						}
					}
				}
			}else{
				array_push($errors, "Campo email vuoto!");
			}

			if(!empty($newDataNascita) && $newDataNascita != $globalRow['DataNascita']){
				$nickname = $_SESSION['nickname'];
				if (DateTime::createFromFormat('Y-m-d', $newDataNascita) === false) { 
					array_push($errors, "Data scelta non disponibile, riprovare"); 
				}else{
					$query = "UPDATE utente SET utente.DataNascita = '$newDataNascita' WHERE utente.Nickname = '$nickname';";
					$results = $mysqli->query($query);
					if($results){
						array_push($errors, "Data aggiornata!");						
					}else{
						array_push($errors, "Errore durante inserimento informazioni nel db [DATA]");
					}
				}
			}

			if(!empty($newNaz) && $newNaz != $globalRow['Nazione']){
				$nickname = $_SESSION['nickname'];
				$query = "UPDATE utente SET utente.Nazione = '$newNaz' WHERE utente.Nickname = '$nickname';";
				$results = $mysqli->query($query);
				if($results){
					array_push($errors, "Nazione aggiornata!");						
				}else{
					array_push($errors, "Errore durante inserimento informazioni nel db [NAZIONE]");
				}
			}
			//TODO AGGIORNA PAGINA
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
			$query = "INSERT INTO utente VALUES('$nickname','$password','$email','$naz','$dataNascita', 0);";
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

	if(isset($req_dbVolteGiocato) && isset($_SESSION['nickname'])){
		if(!isset($_GET['ctrlAction'])){
			$nickname = $_SESSION['nickname'];
			$query = "UPDATE utente SET utente.NumGiocate = utente.NumGiocate + 1 WHERE utente.Nickname = '$nickname';";
			$results = $mysqli->query($query);
			if(!$results){
				echo "Errore durante aggiornamento giocate";
			}

			$query = "SELECT SUM(utente.NumGiocate) AS NumGiocate FROM utente;";
			$results = $mysqli->query($query);

			if ($results->num_rows == 1) {
				$row = $results->fetch_array(MYSQLI_ASSOC);
				$volteGiocato = $row["NumGiocate"];
			}else {
				echo "DB Errore";
			}
		}
	}

?>