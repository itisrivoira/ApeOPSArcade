import { CST } from "../CST.js";
export class CommandsScene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.OPTIONS_COMMANDS
        })
    }
    init(data) {
        console.log(data);
    }
    create() {
        //background
        //this.add.image(this.game.renderer.width / 2, this.game.renderer.height * 0.20, "title").setDepth(1);
        this.add.image(0, 0, "background").setOrigin(0).setDepth(0);

        //labels
        this.add.image(this.game.renderer.width - 655, this.game.renderer.height - 370, "CommandsScene-leftLabel").setDepth(1);
        this.add.image(this.game.renderer.width - 663, this.game.renderer.height / 2.6, "CommandsScene-rightLabel").setDepth(1);
        this.add.image(this.game.renderer.width - 634, this.game.renderer.height / 1.6, "CommandsScene-upLabel").setDepth(1);
        this.add.image(this.game.renderer.width - 660, this.game.renderer.height / 1.2, "CommandsScene-downLabel").setDepth(1);
        this.add.image(this.game.renderer.width - 250, this.game.renderer.height - 370, "CommandsScene-returnLabel").setDepth(1);
        this.add.image(this.game.renderer.width - 289, this.game.renderer.height / 2.6, "CommandsScene-closeLabel").setDepth(1);

        //commands
        this.add.image(this.game.renderer.width - 535, this.game.renderer.height - 370, "CommandsScene-leftarrowkey").setDepth(1);
        this.add.image(this.game.renderer.width - 533, this.game.renderer.height / 2.6, "CommandsScene-rightarrowkey").setDepth(1);
        this.add.image(this.game.renderer.width - 534, this.game.renderer.height / 1.6, "CommandsScene-uparrowkey").setDepth(1);
        this.add.image(this.game.renderer.width - 525, this.game.renderer.height / 1.2, "CommandsScene-downarrowkey").setDepth(1);
        this.add.image(this.game.renderer.width - 120, this.game.renderer.height - 370, "CommandsScene-esc_key").setDepth(1);
        this.add.image(this.game.renderer.width - 119, this.game.renderer.height / 2.6, "CommandsScene-alt_f4_key").setDepth(1);

        //others
        let backButton = this.add.image(this.game.renderer.width / 1.4, this.game.renderer.height / 2 + 150, "OptionsScene-back").setDepth(1);

        //interactive back button
        backButton.setInteractive();

        backButton.on("pointerup", () => {
            console.log("USCITO COMMANDSSCENE");
            this.scene.start(CST.SCENES.OPTIONS, "CommandsScene HELLO");
        });
    }
}