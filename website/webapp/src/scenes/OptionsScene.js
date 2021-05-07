import { CST } from "../CST.js";
export class OptionsScene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.OPTIONS
        })
    }
    init(data) {
        console.log(data);
        this.flagSound = data.flagSound;
    }
    create() {
        //images
        this.add.image(this.game.renderer.width / 2, this.game.renderer.height * 0.20, "title").setDepth(1);
        this.add.image(0, 0, "background").setOrigin(0).setDepth(0);


        let musicButton = this.add.sprite(this.game.renderer.width / 1.5, this.game.renderer.height / 2.3, "OptionsScene-toggleOn").setDepth(1);

        if (this.flagSound == 1) {
            this.soundFlag = true;
            this.flagSound = 0;
        } else {
            musicButton.setTexture("OptionsScene-toggleOff");
        }

        let musicLabel = this.add.image(this.game.renderer.width / 2.4, this.game.renderer.height / 2.3, "OptionsScene-musicLabel").setDepth(1);
        let otherButton = this.add.image(this.game.renderer.width / 1.5, this.game.renderer.height / 1.6, "OptionsScene-toggleOff").setDepth(1);
        let otherLabel = this.add.image(this.game.renderer.width / 3.3, this.game.renderer.height / 1.6, "OptionsScene-effectsLabel").setDepth(1);

        let commandsButton = this.add.image(this.game.renderer.width / 3.3, this.game.renderer.height / 2 + 150, "OptionsScene-commands").setDepth(1);
        let backButton = this.add.image(this.game.renderer.width / 1.4, this.game.renderer.height / 2 + 150, "OptionsScene-back").setDepth(1);

        //interactive buttons
        musicButton.setInteractive();
        commandsButton.setInteractive();
        backButton.setInteractive();

        musicButton.on("pointerup", () => {
            if (this.flagSound == 1) {
                console.log("OptionsScene: toggleOff");
                musicButton.setTexture("OptionsScene-toggleOff");
                this.sound.removeAll();
                this.flagSound = 0;
            } else if (this.flagSound == 0 && this.soundFlag == false) {
                console.log("OptionsScene: toggleOn 1");
                musicButton.setTexture("OptionsScene-toggleOn");
                this.flagSound = 1;
            } else {
                console.log("OptionsScene: toggleOff first");
                musicButton.setTexture("OptionsScene-toggleOff");
                this.sound.removeAll();
                this.flagSound = 0;
                this.soundFlag = false;
            }
        });

        commandsButton.on("pointerup", () => {
            console.log("GOING TO COMMANDS...");
            this.scene.start(CST.SCENES.OPTIONS_COMMANDS, "OptionsScene HELLO");
        })

        backButton.on("pointerup", () => {
            console.log("FUNGE");
            this.scene.start(CST.SCENES.MENU, { HELLO: "OptionsScene HELLO", flagSound: this.flagSound });
        });

    }
}