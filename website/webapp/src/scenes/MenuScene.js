import { CST } from "../CST.js";
export class MenuScene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.MENU
        })
    }
    init(data) {
        console.log(data);
    }
    create() {
        this.game.scale.resize(800, 440);

        //images
        this.add.image(this.game.renderer.width / 2, this.game.renderer.height * 0.20, "title").setDepth(1);
        this.add.image(0, 0, "background").setOrigin(0).setDepth(0);

        //music
        this.sound.pauseOnBlur = false;
        this.sound.play("bgMusic", {
            loop: true
        });


        let playButton = this.add.image(this.game.renderer.width / 2, this.game.renderer.height / 1.7, "play_button").setDepth(1);
        let optionsButton = this.add.image(this.game.renderer.width / 2, this.game.renderer.height / 2 + 150, "options_button").setDepth(1);

        //interactive buttons
        playButton.setInteractive();
        optionsButton.setInteractive();

        playButton.on("pointerup", () => {
            console.log("LET ME IN");
            this.scene.start(CST.SCENES.STARTER, "MenuScene HELLO");
        });

        optionsButton.on("pointerup", () => {
            console.log("GOD DAMNIT");
            this.scene.start(CST.SCENES.OPTIONS, { HELLO: "MenuScene HELLO", flagSound: 1 });
        });
    }
}