<?php
    $req_dbVolteGiocato = 1;
    include("../server/server.php");

    if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION);
		header("location: ../index.php");
	}
?>
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Homepage del progetto APE OPS ARCADE">
    <meta name="author" content="Cherchi Riccardo">
    <!--<link rel="icon" href="favicon.ico">  Non abbiamo ancora una icona |uso futuro|-->

    <title>APE OPS Arcade</title>

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Template custom -->
    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">
    <link href="../css/layout.css" rel="stylesheet">
    <link href="../css/layoutGame.css" rel="stylesheet">
</head>

<?php if (isset($_SESSION['nickname'])): ?>
<script src="lib/phaser.js"></script>
<script type="module" src="src/main.js"></script>
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
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <?php if (isset($_SESSION['nickname'])): ?>
                            <p style="padding-right: 0.5em; text-align:right;">Benvenuto <strong><a href="../html/riepilogoUtente.php?change=1" style="text-decoration: none; color: black;"><?php echo $_SESSION['nickname']; ?></a></strong></p>
			                <p class="logoutButton"> <a href="game.php?logout='1'&ctrlAction=1" style="color: red; text-decoration: none;">LOGOUT</a> </p></div>
		                <?php endif ?>
                    </div>
                </div>
            </div>
        </header>

        <div class="nav-scroller py-1 mb-2">
            <nav class="nav d-flex justify-content-between">
                <a class="p-2 text-muted" href="../index.php">HOME</a>
                <a class="p-2 text-muted" href="../html/download.php">DOWNLOAD</a>
                <a class="p-2 text-muted" href="../html/supporto.php">SUPPORTO TECNICO</a>
                <a class="p-2 text-muted" href="../html/faq.html">FAQ</a>
                <a class="p-2 text-muted" href="../html/contatti.html">CONTATTI</a>
            </nav>
        </div>
    </div>

    <!-- Inizio container main -->
    <main role="main" class="container container-main">
        <div class="row">
            <aside class="col-md-2 sidebar">
                <div class="p-3 mb-3 bg-light rounded">
                    <h4 class="font-italic">Il progetto</h4>
                    <p class="mb-0">Il progetto è nato a seguito della richiesta di una storia che fosse diversa dalle altre, una storia che doveva colpire dritto il cuore del giocatore. La storia doveva poi essere rappresentata sotto forma di gioco interattivo adatto
                        a tutte le età e che avesse come premessa una natura semplice e divertente. Da questa storia nasce <em><b>APE OPS Arcade</b></em></p>
                </div>
            </aside>
            <div class="col-md-10">
                <div class="row">
                    <div id="heading" class="col-md-12">
                        <h2 id="game-name">APE OPS Arcade - Sconfiggi il gorilla stellare</h2>
                        Giocato: <strong id="game-times-played"><?php if(isset($volteGiocato)): echo $volteGiocato;?><?php else: echo "NULL";?><?php endif ?></strong> volte | Voti: ⍟⍟⍟⍟⍟
                        <p class="tags-label">ARCADE</a>
                        <p class="tags-label">2D</p>
                        <p class="tags-label">ACTION</p>
                        <p class="tags-label">WHOLESOME</p>
                        <p class="tags-label">PARODY</p>
                    </div>
                </div>
                <div class="row">
                    <div id="webgame" class="col-md-12">
                        <div>
                            <div id="gameDiv" class="jumbotron text-white rounded bg-dark">
                                <!--<img class="img-fluid" data-src="holder.js/1920x480?theme=thumb" alt="presenza webapp qui"> -->
                            </div>
                            <div id="pulsanti">
                                <i class="fa fa-thumbs-o-up circle-icon"></i>
                                <i class="fa fa-thumbs-o-down circle-icon"></i>

                                <div class="btn-group">
                                    <button class="btn btn-primary btn-lg dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                      Condividi
                                    </button>
                                    <div class="dropdown-menu">
                                        <a class="dropdown-item" href="https://www.facebook.com/sharer/sharer.php?u=http://apeopsarcade.net/game">
                                            <i class="fa fa-facebook-square"></i> Facebook
                                        </a>
                                        <a class="dropdown-item" href="https://twitter.com/intent/tweet?url=http://apeopsarcade.net/game">
                                            <i class="fa fa-twitter-square"></i> Twitter
                                        </a>
                                        <a class="dropdown-item" href="whatsapp://send?text=https://apeopsarcade.net/game">
                                            <i class="fa fa-whatsapp"></i> Whatsapp
                                        </a>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="#">
                                            <i class="fa fa-bug"></i> Segnala
                                        </a>
                                    </div>
                                </div>
                            </div>
                            <div id="istructions">
                                <h4 style="font-family: 'Montserrat', sans-serif;">Come si gioca a APE OPS Arcade - Sconfiggi il gorilla</h4>
                                <img id="game-img-little" class="img-fluid" src="../img/e.png" style="height: 180px; width: 230px;" alt="immagineRandom">
                                <p>
                                    In APE OPS Arcade assumerai il ruolo di uno scienziato i cui esperimenti non sono andati molto bene, il tuo compito è eliminare un gorilla geneticamente mutato che vuole distruggere la Terra.<br> Inoltre incontrerai
                                    durante l'avanzamento nella storia molte creature malevoli che dovrai annientare con ogni attrezzo disponibile per andare avanti nei vari stage.<br><br>Alla fine di ogni stage per avanzare a quello successivo verrai a confronto con un "brigadiere" che ti affronterà in battaglia per fermarti. Ritirarsi dalla battaglia non è contemplato
                                </p>
                                <h5 style="margin-top: 40px; font-family: 'Montserrat', sans-serif;">
                                    <i style="color: #ffffff; background: #4dc862; margin: 0px;" class="fa fa-gamepad circle-icon"></i> COMANDI DI GIOCO
                                </h5>
                                <p style="background: #f0f8ec; padding: 24px; border-radius: 8px;"> Comandi di default (Cambiabili dalle impostazioni all'interno del gioco). Stand-alone only <br><br> “Z” → Attacco base <br>“X” → Attacco pesante <br>“C” → Uso consumabili <br>“ESC” → Aprire menu di
                                    pause<br>“ALT+F4” → Ragequit dopo morte</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <!-- Fine container -->

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
                    <li>Visita la pagina di <a href="../html/faq.html">faq</a></li>
                    <li>e la pagina <a href="../html/contatti.html">contatti</a></li>
                </ol>

                <h4 class="font-italic nomiSviluppatori">Altrove</h4>
                <ol class="list-unstyled">
                    <li><a href="https://github.com/itisrivoira/ApeOPSArcade">GitHub</a></li>
                    <li><a href="https://geti2p.net">I2P</a></li>
                </ol>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JavaScript -->
    <!-- Lo ho messo in fondo in modo che il resto della pagina carichi più velocemente -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>
        window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
    </script>

    <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js"></script>
    <script>
        WebFont.load({
            google: {
                families: ['Droid Sans', 'Droid Serif', 'Quicksand']
            }
        });
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js"></script>
</body>
<?php else:?>
    <body class="bg-dark text-white py-5">
        <div class="container py-5">
            <div class="row">
                <div class="col-md-3 text-center">
                    <p><i class="fa fa-exclamation-triangle fa-5x"></i><br/>Status Code: 403</p>
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
