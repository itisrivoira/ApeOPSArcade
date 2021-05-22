<?php

    session_start();

    if (isset($_GET['logout'])) {
        session_destroy();
        unset($_SESSION);
        header("location: ../index.php");
    }

    
    USE PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;
  
    if(isset($_POST['Invia'])){ 
        // $nick indica il nickname del mittente
        $nick = $_POST['Nickname'];
        // $email indica la mail del mittente
        $email = $_POST['email'];
        //  $testo indica il testo all'interno della mail del mittente
        $testo = $_POST['comment'];

        // $subject indica il titolo della mail
        $subject = 'Recapito supporto tecnico';

        require_once "PHP-MAIL/PHPMailer.php";
        require_once "PHP-MAIL/SMTP.php";
        require_once "PHP-MAIL/POP3.php";
        require_once "PHP-MAIL/Exception.php";

        // creo nuovo oggetto PHPMailer
        $mail = new PHPMailer();

        //Impostazioni SMTP
        $mail->IsSMTP();
        $mail->Host = "smtp.gmail.com"; //imposto come mail host quello di gmail stmp cioè posta uscente
        $mail->SMTPAuth = true; //serve per dire se esiste o no un autenticazione
        $mail->Username = "apeopsarcade@gmail.com";    // metto l'emai di APE SUPPORTO TECNICO
        $mail->Password = "APE20215C"; //password dell account APE
        $mail->Port = 465; //porta del server di posta in uscita(PORTA FISSA DI GMAIL)
        $mail->SMTPSecure = 'ssl';  //serve ad impostare la sicurezza con il protocollo tls

        // Impostazioni email
        $mail->IsHTML();
        $mail->setFrom($email, $nick);
        $mail->AddAddress("apeopsarcade@gmail.com");
        $mail->Subject = ("$email ($subject)"); 
        $mail->Body = $testo;

        if(!$mail->Send()){
            echo "errore nell'invio della mail: ".$mail->ErrorInfo;
        }else{
            header("location: ../index.php");;
        }

    }

?>

<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>


        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <!-- Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

        <!-- Link per il css del login -->
        <link rel="stylesheet" href="../css/layout.css">
        <link rel="stylesheet" href="../css/supporto.css">
    </head>

    <body>
        <div class="container">
            <header class="main-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                        <p></p>
                        <!--Colonna per riempire spazio vuoto-->
                    </div>
                    <div class="col-4 text-center">
                        <a class="main-header-logo text-dark" href="">APE OPS Arcade</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <?php if (!isset($_SESSION['nickname'])): ?>
                            <div class="login">
                                <a href="login.php">
                                    <i class="fa fa-user-circle" id="log-in"></i> Login
                                </a>
                            </div>
                        <?php else:?>
                            <p style="padding-right: 0.5em; text-align:right;">Benvenuto <strong><a href="riepilogoUtente.php?change=1" style="text-decoration: none; color: black;"><?php echo $_SESSION['nickname']; ?></a></strong></p>
			                <p class="logoutButton"> <a href="supporto.php?logout='1'" style="color: red; text-decoration: none;">LOGOUT</a> </p></div>
                        <?php endif ?>
                    </div>
                </div>
            </header>

            <div class="nav-scroller py-1 mb-2">
                <nav class="nav d-flex justify-content-between">
                    <a class="p-2 text-muted" href="../index.php">HOME</a>
                    <a class="p-2 text-muted" href="../webapp/game.php">GAME</a>
                    <a class="p-2 text-muted" href="download.php">DOWNLOAD</a>
                    <a class="p-2 text-muted" href="faq.html">FAQ</a>
                    <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
                </nav>
            </div>
        </div>

        <!-- Immagini contorno-->
        <img src="../img/protagWin.png" class="immagineSinistra">
        <img src="../img/chef.png" class="immagineDestra">

        <div class="contenitorePrincipale">
            <p id="titolo">Supporto APE OPS Arcade</p>
            <div id="intestazione">
                <br> Per inviare un email al supporto tecnico, </br>
                <br> compila il seguente modulo. </br>
            </div>
            <form action="supporto.php" method="post" id="supportForm">
                <div class="supporto">
                    <br>NICKNAME</br>
                    <input type="text" name="Nickname" id="Nickname" placeholder="ilTuoUsername" style="text-align: center;">
                    <br>
                    <br>EMAIL</br>
                    <input type="text" name="email" id="email" placeholder="example@example.com">
                    <br>
                    <br>TESTO</br>
                    <textarea rows="4" cols="" name="comment" form="supportForm" placeholder="Inserisci il testo qui..."></textarea>
                    <br>
                    <br>
                    <input type="submit" name="Invia" value="Invia">
                    <br>
                </div>
            </form>
        </div>

        <footer class="bottom-footer">
            <div class="row">

                <div class="col-md-3">
                    <h2 class="nomiSviluppatori">Sviluppatori: </h2>
                    Riccardo Cherchi<br><p>Miretti Lorenzo<br>Francolino Simone<br>Kevin Kadiasi<br>Stefano Pagliuzzi</p>
                </div>

                <div class="col-md-6">
                    <h2 class="nomiSviluppatori">Il progetto: </h2>
                    <p>Il progetto è nato a seguito della richiesta di una storia che fosse diversa dalle altre,una storia che doveva colpire dritto il cuore del giocatore.La storia doveva poi essere rappresentata sotto forma di gioco interattivo adatto a tutte le età e che avesse come premessa una natura semplice e divertente.</p>
                </div>


                <div class="col-md-3">
                    <h4 class="font-italic nomiSviluppatori">Informazioni Aggiuntive</h4>
                    <ol class="list-unstyled">
                        <li>Visita la pagina di <a href="faq.html">faq</a></li>
                        <li>e la pagina <a href="contatti.html">contatti</a></li>
                    </ol>

                    <h4 class="font-italic nomiSviluppatori">Altrove</h4>
                    <ol class="list-unstyled">
                        <li><a href="https://github.com/itisrivoira/ApeOPSArcade">GitHub</a></li>
                        <li><a href="http://dvgdib2zuodi32qidzh4yb3lu2ohp4z245ns5gmlzroamzcwa4za.b32.i2p/">I2P</a></li>
                    </ol>
                </div>
            </div>
        </footer>

        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script>
            window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
        </script>


        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js "></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js "></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js "></script>



    </body>

</html>
