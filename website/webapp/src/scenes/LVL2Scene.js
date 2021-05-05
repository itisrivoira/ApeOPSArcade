import { CST } from "../CST.js";
export class LVL2Scene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.LEVEL2
        })
        this.hpsProtag = new Array();
        this.hpsEnemy = new Array();
        this.txtHPS = new Array();

        this.checkRound = true;
        this.checkAction = true;

        this.checkEnemy_BlockDodge = 0; //0 -> no | 1 -> Block | 2 -> Dodge
        this.checkProtag_BlockDodge = 0;

        this.maxHpProtag = 6; //MAX HP
        this.maxHpEnemy = 6;

        this.hpEnemyRemaining = this.maxHpEnemy * 2;
        this.hpProtagRemaining = this.maxHpProtag * 2;

        this.protagonist = null;
        this.enemy = null;
    }

    init(data) {
        console.log(data);
    }
    create() {
        //Added enter and exit keys
        this.cursors = this.input.keyboard.createCursorKeys();
        this.keys = this.input.keyboard.addKeys({ 'enter': Phaser.Input.Keyboard.KeyCodes.ENTER, 'exit1': Phaser.Input.Keyboard.KeyCodes.F4, 'exit2': Phaser.Input.Keyboard.KeyCodes.ALT });

        //Main background color
        this.cameras.main.setBackgroundColor("#ccccff");

        //Sets game canvas size to 1280x720
        this.game.scale.resize(1280, 720);


        //Menu images
        let menu = this.add.image(this.game.renderer.width / 2, this.game.renderer.height / 1.2, "LVL2Scene-menu").setDepth(1);
        let attack_1 = this.add.image(this.game.renderer.width - 987, this.game.renderer.height - 163, "LVLScene-menuHiddenButton").setDepth(0);
        let attack_2 = this.add.image(this.game.renderer.width - 702, this.game.renderer.height - 163, "LVLScene-menuHiddenButton").setDepth(1);
        let dodge = this.add.image(this.game.renderer.width - 987, this.game.renderer.height - 78, "LVLScene-menuHiddenButton").setDepth(1);
        let block = this.add.image(this.game.renderer.width - 702, this.game.renderer.height - 78, "LVLScene-menuHiddenButton").setDepth(1);

        let fight = this.add.image(this.game.renderer.width - 322, this.game.renderer.height - 181, "LVLScene-menuHiddenButton").setDepth(1);
        let items = this.add.image(this.game.renderer.width - 322, this.game.renderer.height - 112, "LVLScene-menuHiddenButton2").setDepth(1);
        let quit = this.add.image(this.game.renderer.width - 322, this.game.renderer.height - 55, "LVLScene-menuHiddenButton2").setDepth(1);

        //Menu images setInteractive()
        attack_1.setInteractive();
        attack_2.setInteractive();
        dodge.setInteractive();
        block.setInteractive();
        fight.setInteractive();
        items.setInteractive();
        quit.setInteractive();

        //Protagonist start image
        this.protagonist = this.add.image(this.game.renderer.width / 5.5, this.game.renderer.height / 2.5, "LVLScene-protag").setDepth(0);

        //Enemy start image
        this.enemy = this.add.image(this.game.renderer.width / 1.2, this.game.renderer.height / 2.35, "LVL2Scene-brigadiereMattarella").setDepth(0);

        attack_1.on("pointerup", () => {
            if ((this.checkRound && this.checkAction) && this.hpEnemyRemaining > 0 && this.hpProtagRemaining > 0) {
                this.checkAction = false;

                let text = this.add.text(this.game.renderer.width - 805, 50, "LEGASOV USA LANCIAFIAMME", {
                    fontFamily: "Droid Sans",
                    fontSize: "24px",
                    fill: "#000000"
                });

                this.protagonist.setDepth(1);
                this.protagonist.setPosition(700, this.game.renderer.height / 2.5);
                this.protagonist.setTexture("LVL2Scene-protagActionFire");
                this.enemy.setTexture("LVL2Scene-brigadiereMattarellaHit");

                this.hpEnemyModifier(3);

                this.time.addEvent({
                    delay: 3000,
                    callback: () => {
                        text.destroy();
                        this.checkAction = true;
                        this.checkRound = false;

                        this.protagonist.setDepth(0);
                        this.protagonist.setPosition(this.game.renderer.width / 5.5, this.game.renderer.height / 2.5);
                        this.protagonist.setTexture("LVLScene-protag");
                        this.enemy.setTexture("LVL2Scene-brigadiereMattarella");
                        console.log("PUNCH [protagonista] finito");
                        this.checkEnemy_BlockDodge = 0;
                    }
                });
            }
        });
        attack_2.on("pointerup", () => {
            if ((this.checkRound && this.checkAction) && this.hpEnemyRemaining > 0 && this.hpProtagRemaining > 0) {
                this.checkAction = false;

                let text = this.add.text(this.game.renderer.width - 760, 50, "LEGASOV USA KICK", {
                    fontFamily: "Droid Sans",
                    fontSize: "24px",
                    fill: "#000000"
                });

                this.protagonist.setDepth(1);
                this.protagonist.setPosition(900, this.game.renderer.height / 2.5);
                this.protagonist.setTexture("LVLScene-protagActionKick");
                this.enemy.setTexture("LVL2Scene-brigadiereMattarellaHit");

                this.hpEnemyModifier(2);

                this.time.addEvent({
                    delay: 3000,
                    callback: () => {
                        text.destroy();
                        this.checkAction = true;
                        this.checkRound = false;

                        this.protagonist.setDepth(0);
                        this.protagonist.setPosition(this.game.renderer.width / 5.5, this.game.renderer.height / 2.5);
                        this.protagonist.setTexture("LVLScene-protag");
                        this.enemy.setTexture("LVL2Scene-brigadiereMattarella");
                        console.log("KICK [protagonista] finito");
                        this.checkEnemy_BlockDodge = 0;
                    }
                });
            }
        });
        dodge.on("pointerup", () => {
            if ((this.checkRound && this.checkAction) && this.hpEnemyRemaining > 0 && this.hpProtagRemaining > 0) {
                this.checkAction = false;

                let text = this.add.text(this.game.renderer.width - 760, 50, "LEGASOV SCHIVA", {
                    fontFamily: "Droid Sans",
                    fontSize: "24px",
                    fill: "#000000"
                });

                this.time.addEvent({
                    delay: 3000,
                    callback: () => {
                        text.destroy();
                        this.checkAction = true;
                        this.checkRound = false;
                        console.log("Dodge [protagonista] finito");
                        this.checkProtag_BlockDodge = 3;
                    }
                });
            }
            this.checkEnemy_BlockDodge = 0;
        });
        block.on("pointerup", () => {
            if ((this.checkRound && this.checkAction) && this.hpEnemyRemaining > 0 && this.hpProtagRemaining > 0) {
                this.checkAction = false;

                let text = this.add.text(this.game.renderer.width - 760, 50, "LEGASOV BLOCCA", {
                    fontFamily: "Droid Sans",
                    fontSize: "24px",
                    fill: "#000000"
                });

                this.time.addEvent({
                    delay: 3000,
                    callback: () => {
                        text.destroy();
                        this.checkAction = true;
                        this.checkRound = false;
                        console.log("Block [protagonista] finito");
                        this.checkProtag_BlockDodge = 2;
                    }
                });
            }
            this.checkEnemy_BlockDodge = 0;
        });
        fight.on("pointerup", () => {

        });
        items.on("pointerup", () => {

        });
        quit.on("pointerup", () => {
            this.game.destroy(true, true);
            //this.scene.start(CST.SCENES.MENU, { HELLO: "LVLScene HELLO" });
        });

        //Icons and HP images
        let protagIcon = this.add.image(this.game.renderer.width - 1235, this.game.renderer.height - 685, "LVLScene-protagIcon").setDepth(0);
        let enemyIcon = this.add.image(this.game.renderer.width - 55, this.game.renderer.height - 685, "LVL2Scene-brigadiereMattarellaIcon").setDepth(0);

        let starterWidth = 1170;
        for (let index = 0; index < this.maxHpProtag; index++) {
            this.hpsProtag.push(this.add.image(this.game.renderer.width - starterWidth, this.game.renderer.height - 660, "LVLScene-hpHeartFull").setDepth(0));
            starterWidth = starterWidth - 55;
        }

        starterWidth = 395; //340 with 5 hearts
        for (let index = 0; index < this.maxHpEnemy; index++) {
            this.hpsEnemy.push(this.add.image(this.game.renderer.width - starterWidth, this.game.renderer.height - 660, "LVLScene-hpHeartFull").setDepth(0));
            starterWidth = starterWidth - 55;
        }


        //Protag & enemy names
        this.add.text(this.game.renderer.width - 1195, 8, "KOWALSKY LEGASOV", {
            fontFamily: "Droid Sans",
            fontSize: "32px",
            fill: "#000000"
        });
        this.add.text(this.game.renderer.width - 465, 8, "BRIGADIERE MATTARELLA", {
            fontFamily: "Droid Sans",
            fontSize: "32px",
            fill: "#000000"
        });

        //HPS entities
        this.txtHPS.push(this.add.text(this.game.renderer.width - 1195, 73, "HP: " + this.hpProtagRemaining, {
            fontFamily: "Droid Sans",
            fontSize: "32px",
            fill: "#000000"
        }));
        this.txtHPS.push(this.add.text(this.game.renderer.width - 185, 73, "HP: " + this.hpEnemyRemaining, {
            fontFamily: "Droid Sans",
            fontSize: "32px",
            fill: "#000000"
        }));

    }
    update(time, delta) {
        if (!this.checkRound) {
            let action = Math.floor(Math.random() * 4) + 1;
            let text = null;
            if (this.hpEnemyRemaining > 0) {
                switch (action) {
                    case 1:
                        console.log("Brigadiere attacca con: INCENDIO");
                        this.checkAction = false;

                        text = this.add.text(this.game.renderer.width - 790, 50, "MATTARELLA USA INCENDIO", {
                            fontFamily: "Droid Sans",
                            fontSize: "24px",
                            fill: "#000000"
                        });

                        this.time.addEvent({
                            delay: 1000,
                            callback: () => {
                                this.hpProtagModifier(1);

                                this.enemy.setDepth(1);
                                this.enemy.setPosition(420, this.game.renderer.height / 2.35);
                                this.enemy.setTexture("LVL2Scene-brigadiereMattarellaFire");
                            }
                        });


                        this.time.addEvent({
                            delay: 3000,
                            callback: () => {
                                this.checkAction = true;

                                this.enemy.setDepth(0);
                                this.enemy.setPosition(this.game.renderer.width / 1.2, this.game.renderer.height / 2.35);
                                this.enemy.setTexture("LVL2Scene-brigadiereMattarella");

                                text.destroy();
                                this.checkProtag_BlockDodge = 0;
                            }
                        });
                        break;
                    case 2:
                        console.log("Brigadiere attacca con: Calcio");
                        this.checkAction = false;

                        text = this.add.text(this.game.renderer.width - 760, 50, "MATTARELLA USA KICK", {
                            fontFamily: "Droid Sans",
                            fontSize: "24px",
                            fill: "#000000"
                        });

                        this.time.addEvent({
                            delay: 1000,
                            callback: () => {
                                this.hpProtagModifier(2);

                                this.enemy.setDepth(1);
                                this.enemy.setPosition(330, this.game.renderer.height / 2.35);
                                this.enemy.setTexture("LVL2Scene-brigadiereMattarellaHit");
                            }
                        });

                        this.time.addEvent({
                            delay: 3000,
                            callback: () => {
                                this.checkAction = true;

                                this.enemy.setDepth(0);
                                this.enemy.setPosition(this.game.renderer.width / 1.2, this.game.renderer.height / 2.35);
                                this.enemy.setTexture("LVL2Scene-brigadiereMattarella");

                                text.destroy();
                                this.checkProtag_BlockDodge = 0;
                            }
                        });
                        break;
                    case 3:
                        console.log("Brigadiere schiva");
                        this.checkAction = false;

                        text = this.add.text(this.game.renderer.width - 760, 50, "MATTARELLA SCHIVA", {
                            fontFamily: "Droid Sans",
                            fontSize: "24px",
                            fill: "#000000"
                        });

                        this.time.addEvent({
                            delay: 3000,
                            callback: () => {
                                this.checkAction = true;
                                text.destroy();
                            }
                        });
                        this.checkEnemy_BlockDodge = 3;
                        this.checkProtag_BlockDodge = 0;
                        break;
                    case 4:
                        console.log("Brigadiere blocca");
                        this.checkAction = false;

                        text = this.add.text(this.game.renderer.width - 760, 50, "MATTARELLA BLOCCA", {
                            fontFamily: "Droid Sans",
                            fontSize: "24px",
                            fill: "#000000"
                        });

                        this.time.addEvent({
                            delay: 3000,
                            callback: () => {
                                this.checkAction = true;
                                text.destroy();
                            }
                        });
                        this.checkEnemy_BlockDodge = 2;
                        this.checkProtag_BlockDodge = 0;
                        break;
                }
                this.checkRound = true;
            } else {
                let youWon = this.add.image(this.game.renderer.width - 640, this.game.renderer.height - 450, "youWon").setDepth(1);
                /*youWon.setInteractive();
                youWon.on("pointerup", () => {
                    this.scene.start(CST.SCENES.LEVEL2, { HELLO: "LVLScene HELLO" });
                });*/
                this.enemy.destroy();
                this.protagonist.setTexture("LVLScene-protagActionWin");
            }
        }
        if (this.hpProtagRemaining <= 0) {
            let text = this.add.text(this.game.renderer.width - 760, 50, "HAI PERSO", {
                fontFamily: "Droid Sans",
                fontSize: "50px",
                fill: "#000000"
            });
            this.protagonist.destroy();
        }
    }
    hpEnemyModifier(damage) {
        console.log("HP iniziali nemico: " + this.hpEnemyRemaining);
        console.log("Block/dodge: " + this.checkEnemy_BlockDodge);
        if (this.hpEnemyRemaining > 0) {
            let heartsRemaining = 0;
            if (this.checkEnemy_BlockDodge == 2) {
                heartsRemaining = this.hpEnemyRemaining - damage / 2;
                //Da aggiungere
            } else if (this.checkEnemy_BlockDodge == 3) {
                heartsRemaining = this.hpEnemyRemaining;
            } else {
                heartsRemaining = this.hpEnemyRemaining - damage;
            }
            if (heartsRemaining <= 0) {
                console.log("morto nemico");
                this.hpEnemyRemaining = heartsRemaining;

                for (let index = 0; index < this.hpsEnemy.length; index++) {
                    this.hpsEnemy[index].setTexture("LVLScene-hpHeartEmpty");
                }
                //Da aggiungere schermata endScene
            } else {
                this.heartsCalculator(heartsRemaining, 1);
            }
            this.txtHPS[1].setText("HP: " + this.hpEnemyRemaining);
        }
    }
    hpProtagModifier(damage) {
        console.log("HP iniziali protagonista: " + this.hpProtagRemaining);
        if (this.hpProtagRemaining > 0) {
            let heartsRemaining = 0;
            if (this.checkProtag_BlockDodge == 2) {
                heartsRemaining = this.hpProtagRemaining - damage / 2;
                //Da aggiungere
            } else if (this.checkProtag_BlockDodge == 3) {
                heartsRemaining = this.hpProtagRemaining;
            } else {
                heartsRemaining = this.hpProtagRemaining - damage;
            }
            if (heartsRemaining <= 0) {
                console.log("morto protagonista");
                this.hpProtagRemaining = heartsRemaining;

                for (let index = 0; index < this.hpsEnemy.length; index++) {
                    this.hpsProtag[index].setTexture("LVLScene-hpHeartEmpty");
                }
                //Da aggiungere schermata endScene
            } else {
                this.heartsCalculator(heartsRemaining, 2);
            }
            this.txtHPS[0].setText("HP: " + this.hpProtagRemaining);
        }
    }
    heartsCalculator(heartsRemaining, type) {
        if (type == 1) {
            console.log("HP rimanenti nemico: " + heartsRemaining);
            for (let index = 1; index < heartsRemaining + 1; index++) {
                //console.log("PrimoFOR: " + index);
                switch (index) {
                    case 1:
                        this.hpsEnemy[5].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 2:
                        this.hpsEnemy[5].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 3:
                        this.hpsEnemy[4].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 4:
                        this.hpsEnemy[4].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 5:
                        this.hpsEnemy[3].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 6:
                        this.hpsEnemy[3].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 7:
                        this.hpsEnemy[2].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 8:
                        this.hpsEnemy[2].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 9:
                        this.hpsEnemy[1].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 10:
                        this.hpsEnemy[1].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 11:
                        this.hpsEnemy[0].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 12:
                        this.hpsEnemy[0].setTexture("LVLScene-hpHeartFull");
                        break;
                }
            }
            for (let index = 12; index > heartsRemaining; index--) {
                //console.log("SecondoFOR: " + index);
                switch (index) {
                    case 12:
                        this.hpsEnemy[0].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 11:
                        this.hpsEnemy[0].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 10:
                        this.hpsEnemy[1].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 9:
                        this.hpsEnemy[1].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 8:
                        this.hpsEnemy[2].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 7:
                        this.hpsEnemy[2].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 6:
                        this.hpsEnemy[3].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 5:
                        this.hpsEnemy[3].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 4:
                        this.hpsEnemy[4].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 3:
                        this.hpsEnemy[4].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 2:
                        this.hpsEnemy[5].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 1:
                        this.hpsEnemy[5].setTexture("LVLScene-hpHeartEmpty");
                        break;
                }
                this.hpEnemyRemaining = heartsRemaining;
            }
        } else {
            //Da correggere (cuori invertiti)
            console.log("HP rimanenti protagonista: " + heartsRemaining);
            for (let index = 1; index < heartsRemaining + 1; index++) {
                //console.log("PrimoFOR: " + index);
                switch (index) {
                    case 1:
                        this.hpsProtag[0].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 2:
                        this.hpsProtag[0].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 3:
                        this.hpsProtag[1].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 4:
                        this.hpsProtag[1].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 5:
                        this.hpsProtag[2].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 6:
                        this.hpsProtag[2].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 7:
                        this.hpsProtag[3].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 8:
                        this.hpsProtag[3].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 9:
                        this.hpsProtag[4].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 10:
                        this.hpsProtag[4].setTexture("LVLScene-hpHeartFull");
                        break;
                    case 11:
                        this.hpsProtag[5].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 12:
                        this.hpsProtag[5].setTexture("LVLScene-hpHeartFull");
                        break;
                }
            }
            for (let index = 12; index > heartsRemaining; index--) {
                //console.log("SecondoFOR: " + index);
                switch (index) {
                    case 12:
                        this.hpsProtag[5].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 11:
                        this.hpsProtag[5].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 10:
                        this.hpsProtag[4].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 9:
                        this.hpsProtag[4].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 8:
                        this.hpsProtag[3].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 7:
                        this.hpsProtag[3].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 6:
                        this.hpsProtag[2].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 5:
                        this.hpsProtag[2].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 4:
                        this.hpsProtag[1].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 3:
                        this.hpsProtag[1].setTexture("LVLScene-hpHeartEmpty");
                        break;
                    case 2:
                        this.hpsProtag[0].setTexture("LVLScene-hpHeartHalf");
                        break;
                    case 1:
                        this.hpsProtag[0].setTexture("LVLScene-hpHeartEmpty");
                        break;
                }
                this.hpProtagRemaining = heartsRemaining;
            }
        }
    }
}