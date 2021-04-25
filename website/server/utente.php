<?php

class Utente{
	public function __construct($nick, $mail,$naz,$nasc,$pasw) {
	        $this->nick = $nick;	#nickname
	        $this->email = $mail;	#email
	        $this->naz = $naz;	#nazionalità
	        $this->nasc = $nasc;	#nascità
	        $this->pasw = $pasw;	#password
	}
		
	#get	
	public function getNickname(){
		return $this->nick;
	}
	
	public function getMail(){
		return $this->email;
	}
	
	public function getNascita(){
		return $this->nasc;
	}
	
	public function getNazione(){
		return $this->naz;
	}
	
	public function getPasw(){
		return $this->pasw;
	}
	
	
	#set
	public function setNickname($nick){
		$this->nick=$nick;
	}
	
	public function setMail($mail){
		$this->email=$mail;
	}
	
	public function setDataN($nasc){
		$this->nasc=$nasc;
	}
	
	public function setNazione($naz){
		$this->naz=$naz;
	}
	
	public function setPasw($pasw){
		$this->pasw=$pasw;
	}
	
}
	


?>
