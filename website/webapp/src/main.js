import { LoadScene } from "./scenes/LoadScene.js";
import { MenuScene } from "./scenes/MenuScene.js";
import { OptionsScene } from "./scenes/OptionsScene.js";
let game = new Phaser.Game({
    width: 800,
    height: 440,
    parent: 'gameDiv',
    scene: [
        LoadScene, MenuScene, OptionsScene
    ]
})