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


        let musicButton = this.add.sprite(this.game.renderer.width / 1.5, this.game.renderer.height / 1.7, "OptionsScene-toggleOn").setDepth(1);
        let musicLabel = this.add.image(this.game.renderer.width / 2.4, this.game.renderer.height / 1.7, "OptionsScene-musicLabel").setDepth(1);
        let otherButton = this.add.image(this.game.renderer.width / 1.5, this.game.renderer.height / 2 + 150, "OptionsScene-toggleOff").setDepth(1);
        let otherLabel = this.add.image(this.game.renderer.width / 3.3, this.game.renderer.height / 2 + 150, "OptionsScene-effectsLabel").setDepth(1);

        //interactive buttons
        musicButton.setInteractive();
        otherButton.setInteractive();

        musicButton.on("pointerup", () => {
            if (this.flagSound == 1) {
                musicButton.setTexture("OptionsScene-toggleOff");
                this.sound.removeAll();
                this.flagSound = 0;
            } else {
                musicButton.setTexture("OptionsScene-toggleOn");
                //music
                this.sound.pauseOnBlur = false;
                this.sound.play("bgMusic", {
                    loop: true
                });
                this.flagSound = 1;
            }
        });

        otherButton.on("pointerup", () => {
            console.log("FUNGE");
            this.scene.start(CST.SCENES.MENU, "OptionsScene HELLO");
        });

    }
}