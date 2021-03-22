import { CST } from "../CST.js";
export class LVLScene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.STARTER
        })
        this.map = null;
        this.player = null;
        this.text = null;
        this.score = 0;
        this.groundLayer = null;
        this.coinLayer = null;
        this.cursors = null;
    }

    init(data) {
        console.log(data);
    }
    create() {
        //load map
        this.map = this.make.tilemap({ key: "map" });

        //ground tiles
        var groundTiles = this.map.addTilesetImage("tiles");

        //create ground layer
        this.groundLayer = this.map.createDynamicLayer("World", groundTiles, 0, 0);

        //player collision with layer
        this.groundLayer.setCollisionByExclusion([-1]);

        var coinTiles = this.map.addTilesetImage('coin');
        this.coinLayer = this.map.createDynamicLayer('Coins', coinTiles, 0, 0)

        //game world boundaries
        this.physics.world.bounds.width = this.groundLayer.width;
        this.physics.world.bounds.height = this.groundLayer.height;

        //player sprite    
        this.player = this.physics.add.sprite(200, 200, "player");
        this.player.setBounce(0.2); //player will bounce from items
        this.player.setCollideWorldBounds(true); //collide with boundaries

        this.player.body.setSize(this.player.width, this.player.height - 8)

        //collider player/groundLayer
        this.physics.add.collider(this.groundLayer, this.player);

        // player walk animation
        this.anims.create({
            key: "walk",
            frames: this.anims.generateFrameNames("player", { prefix: "p1_walk", start: 1, end: 11, zeroPad: 2 }),
            frameRate: 10,
            repeat: -1
        });
        //idle with only one frame
        this.anims.create({
            key: "idle",
            frames: [{ key: "player", frame: "p1_stand" }],
            frameRate: 10,
        });

        this.coinLayer.setTileIndexCallback(17, this.collectCoin, this);
        //when the player overlaps with a tile with index 17

        this.physics.add.overlap(this.player, this.coinLayer);

        //keys
        this.cursors = this.input.keyboard.createCursorKeys();

        //bounds
        this.cameras.main.setBounds(0, 0, this.map.widthInPixels, this.map.heightInPixels);

        this.cameras.main.startFollow(this.player);

        //background color   
        this.cameras.main.setBackgroundColor("#ccccff");
        this.text = this.add.text(20, 20, "0", {
            fontSize: "40px",
            fill: "#ffffff"
        });
        this.text.setScrollFactor(0);

    }
    update(time, delta) {
        if (this.cursors.left.isDown) {
            this.player.body.setVelocityX(-200);
            this.player.anims.play('walk', true); //walk animation
            this.player.flipX = true;
        } else if (this.cursors.right.isDown) {
            this.player.body.setVelocityX(200);
            this.player.anims.play("walk", true);
            this.player.flipX = false;
        } else {
            this.player.body.setVelocityX(0);
            this.player.anims.play("idle", true)
        }
        if ((this.cursors.space.isDown || this.cursors.up.isDown) && this.player.body.onFloor()) {
            this.player.body.setVelocityY(-500); //jump
        }
    }
    collectCoin(sprite, tile) {
        this.coinLayer.removeTileAt(tile.x, tile.y); //remove coin
        this.score++;
        this.text.setText(this.score);
        return false;
    }
}