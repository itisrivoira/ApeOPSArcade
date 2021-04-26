import { LoadScene } from "./scenes/LoadScene.js";
import { MenuScene } from "./scenes/MenuScene.js";
import { OptionsScene } from "./scenes/OptionsScene.js";
import { CommandsScene } from "./scenes/CommandsScene.js";
import { LVLScene } from "./scenes/LVLScene.js";
import { LVL2Scene } from "./scenes/LVL2Scene.js";
let game = new Phaser.Game({
    width: 800,
    height: 440,
    parent: 'gameDiv',
    physics: {
        default: 'arcade',
        arcade: {
            //gravity: { y: 400 },
            debug: false
        }
    },
    scene: [
        LoadScene, MenuScene, LVLScene, LVL2Scene, OptionsScene, CommandsScene
    ]
});