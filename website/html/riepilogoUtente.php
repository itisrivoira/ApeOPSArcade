<?php
    include("../server/server.php");

    if (isset($_GET['logout'])) {
        session_destroy();
        unset($_SESSION);
        header("location: ../index.php");
    }
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Riepilogo Utente</title>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Link per il css del login -->
    <link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/riepilogoUtente.css">
</head>

<?php if (isset($_SESSION['nickname'])): ?>
    <body>
        <div class="container">
            <header class="main-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                        <p></p>
                        <!--Colonna per riempire spazio vuoto-->
                    </div>
                    <div class="col-4 text-center">
                        <a class="main-header-logo text-dark" href="#">APE OPS Arcade</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <p style="padding-right: 0.5em; text-align:right;">Benvenuto <strong><a href="riepilogoUtente.php?change=1" style="text-decoration: none; color: black;"><?php echo $_SESSION['nickname']; ?></a></strong></p>
                        <p class="logoutButton"> <a href="riepilogoUtente.php?logout='1'" style="color: red; text-decoration: none;">LOGOUT</a> </p>
                    </div>
                </div>
            </header>

            <div class="nav-scroller py-1 mb-2">
                <nav class="nav d-flex justify-content-between">
                    <a class="p-2 text-muted" href="../index.php">HOME</a>
                    <a class="p-2 text-muted" href="../webapp/game.php">GAME</a>
                    <a class="p-2 text-muted" href="download.php">DOWNLOAD</a>
                    <a class="p-2 text-muted" href="supporto.php">SUPPORTO TECNICO</a>
                    <a class="p-2 text-muted" href="faq.html">FAQ</a>
                    <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
                </nav>
            </div>

            <div class="layout">
                <div class="row">
                    <div class="col-md-12">
                        <div class="titolo"> MODIFICA INFORMAZIONI</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4">
                        <?php include("../server/errors.php");?>
                        <form action="riepilogoUtente.php?change=1" method="POST">
                            <div class="formatCarattare">Nickname: <br><input type="text" name="nickname" <?php if(!isset($nicknameResult)):?>placeholder="Non specificato"<?php else:?>value=<?php echo $nicknameResult?><?php endif ?>></div>
                            <br>
                            <div class="formatCarattare">Email: <br><input type="text" name="email" <?php if(!isset($emailResult)):?>placeholder="Non specificato"<?php else:?>value=<?php echo $emailResult?><?php endif ?>></div>
                            <br>
                            <div class="formatCarattare">Nazionalità: 
                            <br>
                            <select name="naz">
                                <option value="NAN" disabled selected>Non specificato</option>
                                <option value="ARG"<?php if (isset($nazResult)){ if($nazResult == 'ARG'){ echo ' selected="selected"';}} ?>>Argentina</option>
                                <option value="AUS"<?php if (isset($nazResult)){ if($nazResult == 'AUS'){ echo ' selected="selected"';}} ?>>Australia</option>
                                <option value="BRA"<?php if (isset($nazResult)){ if($nazResult == 'BRA'){ echo ' selected="selected"';}} ?>>Brazil</option>
                                <option value="CAN"<?php if (isset($nazResult)){ if($nazResult == 'CAN'){ echo ' selected="selected"';}} ?>>Canada</option>
                                <option value="CHN"<?php if (isset($nazResult)){ if($nazResult == 'CHN'){ echo ' selected="selected"';}} ?>>China</option>
                                <option value="FRA"<?php if (isset($nazResult)){ if($nazResult == 'FRA'){ echo ' selected="selected"';}} ?>>France</option>
                                <option value="DEU"<?php if (isset($nazResult)){ if($nazResult == 'DEU'){ echo ' selected="selected"';}} ?>>Germany</option>
                                <option value="IND"<?php if (isset($nazResult)){ if($nazResult == 'IND'){ echo ' selected="selected"';}} ?>>India</option>
                                <option value="ITA"<?php if (isset($nazResult)){ if($nazResult == 'ITA'){ echo ' selected="selected"';}} ?>>Italy</option>
                                <option value="ENG"<?php if (isset($nazResult)){ if($nazResult == 'ENG'){ echo ' selected="selected"';}} ?>>England</option>
                                <option value="JPN"<?php if (isset($nazResult)){ if($nazResult == 'JPN'){ echo ' selected="selected"';}} ?>>Japan</option>
                                <option value="NLD"<?php if (isset($nazResult)){ if($nazResult == 'NLD'){ echo ' selected="selected"';}} ?>>Netherlands</option>
                                <option value="USA"<?php if (isset($nazResult)){ if($nazResult == 'USA'){ echo ' selected="selected"';}} ?>>United States</option>
                            </select></div>
                            <br>
                            <div class="formatCarattare">Anno⠀di⠀Nascita: <br><input type="date" name="dataN" <?php if(isset($dataResult)):?>value=<?php echo $dataResult?><?php endif ?>></div>
                            <br>
                            <div class="formatCarattare">Password: <br><input type="password" name="password_1" placeholder="Password..."></div>
                            <br>
                            <div class="formatCarattare">Conferma⠀Password: <br><input type="password" name="password_2" placeholder="Conferma password..."></div>
                            <br>
                            <input type="submit" class="formatCarattare" value="CANCELLA">
                            <input type="submit" class="formatCarattare" name="salva" value="SALVA">
                        <form>
                    </div>

                    <div class="col-md-8">
                        <img src="../img/protagKick.png" class="img">
                    </div>
                </div>
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
                            <li>Visita la pagina di <a href="html/faq.html">faq</a></li>
                            <li>e la pagina <a href="html/contatti.html">contatti</a></li>
                        </ol>

                        <h4 class="font-italic nomiSviluppatori">Altrove</h4>
                        <ol class="list-unstyled">
                            <li><a href="https://github.com/itisrivoira/ApeOPSArcade">GitHub</a></li>
                            <li><a href="http://dvgdib2zuodi32qidzh4yb3lu2ohp4z245ns5gmlzroamzcwa4za.b32.i2p/">I2P</a></li>
                        </ol>
                    </div>
                </div>
            </footer>
        </div>




        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script>
            window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
        </script>


        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js "></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js "></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js "></script>




    </body>
<?php else: ?>
    <body class="bg-dark text-white py-5">
        <div class="container py-5">
            <div class="row">
                <div class="col-md-3 text-center">
                    <p id="immagineAlert"><i class="fa fa-exclamation-triangle fa-5x" id="immagineAlert"></i><br/>Status Code: 403</p>
                </div>
                <div class="col-md-9">
                    <h3>OPPSSS!!!! Sorry...</h3>
                    <p>Per poter accedere alla pagina hai bisogno di eseguire prima il login<br/>Perfavore esegui il login e riprova</p>
                    <a class="btn btn-danger" href="javascript:history.back()">Torna indietro</a>
                </div>
            </div>
        </div>
    </body>
<?php endif ?>

</html>