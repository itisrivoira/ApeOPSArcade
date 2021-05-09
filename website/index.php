<?php
    session_start();

    if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION);
		header("location: index.php");
	}
?>
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Homepage del progetto APE OPS ARCADE">
    <meta name="author" content="Cherchi Riccardo & Miretti Lorenzo">
    <!--<link rel="icon" href="favicon.ico">  Non abbiamo ancora una icona |uso futuro|-->

    <title>APE OPS Arcade</title>

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Template custom -->
    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">
    <link href="css/layout.css" rel="stylesheet">
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
                    <a class="main-header-logo text-dark" href="#">APE OPS Arcade</a>
                </div>
                <div class="col-4 d-flex justify-content-end align-items-center">
                    <?php if (!isset($_SESSION['nickname'])): ?>
                        <div class="login">
                            <a href="html/login.php">
                                <i class="fa fa-user-circle" id="log-in"></i> Login
                            </a>
                        </div>
                    <?php else:?>
                        <p style="padding-right: 0.5em; text-align:right;">Benvenuto <strong><a href="html/riepilogoUtente.php?change=1" style="text-decoration: none; color: black;"><?php echo $_SESSION['nickname']; ?></a></strong></p>
			            <p class="logoutButton"> <a href="index.php?logout='1'" style="color: red; text-decoration: none;">LOGOUT</a> </p></div>
		            <?php endif ?>
                </div>
            </div>
        </header>

        <div class="nav-scroller py-1 mb-2">
            <nav class="nav d-flex justify-content-between">
                <a class="p-2 text-muted" href="webapp/game.php">GAME</a>
                <a class="p-2 text-muted" href="html/download.php">DOWNLOAD</a>
                <a class="p-2 text-muted" href="html/supporto.php">SUPPORTO TECNICO</a>
                <a class="p-2 text-muted" href="html/faq.html">FAQ</a>
                <a class="p-2 text-muted" href="html/contatti.html">CONTATTI</a>
            </nav>
        </div>

        <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark">
            <div class="row">
                <div class="col-md-6 px-0">
                    <h1 class="display-4 font-italic">APE OPS ARCADE</h1>
                    <p class="lead my-3">Ape OPS Arcade è un gioco single-player action-driven side-scrolling 2D dove il tuo compito sarà sconfiggere il Gorilla Stellare utilizzando ogni arma ed oggetto a tua disposizione. Il tempo a tua disposizione non è molto, su muoviti
                        ed uccidi quella scimmietta da quattro soldi prima che sia lei ad uccidere te…</p>
                    <br>
                    <p class="lead mb-0"><a href="#introduzione" class="text-white font-weight-bold">Vai all'introduzione...</a></p>
                </div>
                <div class="col-md-6 px-0">
                    <img src="img/ape_logo.png" class="img-fluid" alt="Responsive image">
                </div>
            </div>
        </div>

        <!-- Inizio cards -->
        <div class="row mb-2">
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                        <strong class="d-inline-block mb-2 text-primary">FAQ</strong>
                        <h3 class="mb-0">
                            <a class="text-dark" href="#">Domande frequenti</a>
                        </h3>
                        <p class="card-text mb-auto">C'è qualcosa che non riesci a comprendere? Visita le FAQ per trovare la soluzione.</p>
                        <a href="#">Vai alle FAQ</a>
                    </div>
                    <img class="trumbnail-example card-img-right flex-auto d-none d-md-block" data-src="holder.js/200x250?theme=thumb" alt="Card image cap">
                </div>
            </div>
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                        <strong class="d-inline-block mb-2 text-success">AGGIORNAMENTO</strong>
                        <h3 class="mb-0">
                            <a class="text-dark" href="#">Aggiornamento 0.5</a>
                        </h3>
                        <div class="mb-1 text-muted">Mar 26</div>
                        <p class="card-text mb-auto">Modifiche al website e nuove features sono in arrivo!</p>
                        <a href="#aggiornamento">Vai all'aggiornamento</a>
                    </div>
                    <img class="trumbnail-example card-img-right flex-auto d-none d-md-block" data-src="holder.js/200x250?theme=thumb" alt="Card image cap">
                </div>
            </div>
        </div>
        <!-- Fine cards -->
    </div>

    <!-- Inizio container main -->
    <main role="main" class="container">
        <!-- Inizio riga -->
        <div class="row">
            <!-- Inizio scheda post -->
            <div class="col-md-8 container-main">
                <h3 class="pb-3 mb-4 font-italic border-bottom" id="introduzione">
                    Dal dream Team
                </h3>

                <!-- Inizio post -->
                <div class="container-post">
                    <h2 class="container-post-title">Introduzione</h2>
                    <p> </p>

                    <p>In APE OPS Arcade assumerai il ruolo di uno scienziato i cui esperimenti non sono andati molto bene, il tuo compito è eliminare un gorilla geneticamente mutato che vuole distruggere la Terra.</p>
                    <hr>
                    <p>Attraverserai luoghi impervi dove le tue abilità saranno messe a dura prova, il tempo rappresenta la tua capacità di annientare nemici ed è di vitale importanza. Fuori nella natura vari mostri corrotti sono stati creati e reclutati
                        dal Gorilla Stellare per rallentare la tua avanzata ed è tua necessità affrontarli per evitare che milioni di persone muoiano in quella che viene vista come l'incarnazione dell'esplosione di una stella.</p>
                    <h3>Regole base</h3>
                    <p>Dopo una breve cutscene verrai direttamente scaraventato nel mondo corrotto di APE OPS Arcade. Qui incontrerai durante l'avanzamento nella storia molte creature malevoli che dovrai annientare con ogni attrezzo disponibile per andare
                        avanti nei vari stage.</p>
                    <p></p>
                    <p>Quando metti a segno un colpo questo ha una media probabilità di diventare critico infliggendo danni doppi al mostro interessato. Ogni creatura sconfitta rilascerà dei punti EXP ed una valuta chiamata "Kharal" che potrà essere utilizzata
                        per acquistare oggetti di supporto venduti da mercanti. Alla fine di ogni stage per avanzare a quello successivo verrai a confronto con un "brigadiere" che ti affronterà in battaglia per fermarti.</p>
                    <p>Ritirarsi dalla battaglia non è contemplato</p>

                    <h3>Comandi di gioco</h3>
                    <p>I comandi sono una parte essenziale del gioco, per questo conviene cambiarli per adeguarli alle proprie preferenze ma di default sono stati pensati per offrire un controllo semplice al giocatore, anche se questo si trova alle prime
                        armi con un Arcade</p>
                    <p>Comandi di default (Cambiabili dalle impostazioni all'interno del gioco). PC Only</p>
                    <ul>
                        <li>“Z” → Attacco base</li>
                        <li>“X” → Attacco pesante</li>
                        <li>“C” → Uso consumabili</li>
                        <li>“BARRA SPAZIATRICE” → Salto</li>
                        <li>“ESC” → Aprire menu di pause</li>
                        <li>“Q” → Attacco Ultimate™</li>
                        <li>“ALT+F4” → Ragequit dopo morte</li>
                    </ul>
                    <p>Nella versione mobile a posto dei tasti vi sono pulsanti facilmente cliccabili con icone intuitive o scritte per guidarti nel districato mondo dei comandi.
                    </p>
                </div>
                <!-- Fine post -->

                <hr>
                <hr id="aggiornamento">
                <!-- Inizio post -->
                <div class="container-post">
                    <h2 class="container-post-title">Aggiornamento 0.4</h2>
                    <p class="container-post-meta">20 Febbraio 2021</p>

                    <p>-- PROVA --</p>
                    <p>Un anno fa, il 20 febbraio 2020, l'Italia conosce il suo primo caso accertato di Covid-19. Quando ancora si pensava che il virus fosse troppo lontano per raggiungerci, a Codogno, paese nella Bassa Lodigiana, una dottoressa decide di
                        non seguire i protocolli e scopre così l'esistenza del Paziente 1, il 38enne Mattia Maestri. Il giorno dopo si registra il primo morto da coronavirus.</p>
                    <p>-- FINE PROVA --</p>
                    <ul>
                        <li>Creazione pagine da affiancare alla homepage.</li>
                        <li>Gestione endpoints con Express(Node JS).</li>
                        <li>Creazione login page e registration page.</li>
                    </ul>
                    <p>Il dream Team è sempre impegnato a migliorare l'esperienza dell'utente, ogni aggiornamento porterà nuove features e correzioni.</p>
                    <p>--qualcosa in latino per riempire--</p>
                    <p>Donec ullamcorper nulla non metus auctor fringilla. Nulla vitae elit libero, a pharetra augue.</p>
                </div>
                <!-- Fine post -->
            </div>
            <!-- Fine scheda post -->

            <!-- Inizio sidebar -->
            <aside class="col-md-4 container-sidebar">
                <div class="p-3 mb-3 bg-light rounded">
                    <h4 class="font-italic">Il progetto</h4>
                    <p class="mb-0">Il progetto è nato a seguito della richiesta di una storia che fosse diversa dalle altre, una storia che doveva colpire dritto il cuore del giocatore. La storia doveva poi essere rappresentata sotto forma di gioco interattivo adatto
                        a tutte le età e che avesse come premessa una natura semplice e divertente. Da questa storia nasce <em><b>APE OPS Arcade</b></em></p>
                </div>

                <div class="p-3">
                    <h4 class="font-italic">Altrove</h4>
                    <ol class="list-unstyled">
                        <li><a href="https://github.com/itisrivoira/ApeOPSArcade">GitHub</a></li>
                        <li><a href="https://geti2p.net">I2P</a></li>
                        <li><a href="#">Facebook(?)</a></li>
                    </ol>
                </div>
            </aside>
            <!-- Fine sidebar -->

        </div>
        <!-- Fine riga -->

    </main>
    <!-- Fine container -->

    <footer class="bottom-footer">
        <p>Creato e modificato da <a href="https://github.com/Cherchuzo">Cherchuzo</a> e <a href="https://github.com/lollomire">lollomire</a>.</p>
        <p>
            <a href="">Torna all'inizio</a>
        </p>
    </footer>

    <!-- Bootstrap JavaScript -->
    <!-- Lo ho messo in fondo in modo che il resto della pagina carichi più velocemente -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>
        window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js"></script>
    <script>
        //Aggiunta Holder via mancanza immagini da piazzare
        Holder.addTheme('thumb', {
            bg: '#55595c',
            fg: '#eceeef',
            text: 'Thumbnail'
        });

        /*var trumbImages = document.getElementsByClassName("trumbnail-example");

        while (true) {
            if (screen.width >= 1920) {
                trumbImages[0].setAttribute("data-src", "holder.js/200x300?theme=thumb");
                trumbImages[1].setAttribute("data-src", "holder.js/200x300?theme=thumb");
            } else {
                trumbImages[0].setAttribute("data-src", "holder.js/200x250?theme=thumb");
                trumbImages[1].setAttribute("data-src", "holder.js/200x250?theme=thumb");
            }
        }*/
    </script>
</body>

</html>