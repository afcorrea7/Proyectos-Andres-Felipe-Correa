/*
    Rata Lab - Andrés Felipe Correa
    2023
*/

using UnityEngine;
using System.Collections;

public class ControllerRat : MonoBehaviour {

	public float speed;
	[Header("Element 0 for turn speed, Element 1 for multiplier")]
	public float[] turnSpeedParameters = {8, 15};
	float horizontalInput;
    float verticalInput;
	bool freeToMove=true; //Start by being able to move
   	private Rigidbody playerRB;
	
	void Start () {
		playerRB=GetComponent<Rigidbody>();
	}
	
	void FixedUpdate() {
		if(freeToMove){
			PlayerMovement();
			PlayerRotation();
		}
	}

	void PlayerMovement(){
    	verticalInput = Input.GetAxisRaw("Vertical")*speed*Time.deltaTime;
        playerRB.position += (transform.forward *verticalInput);
	}

	void PlayerRotation(){ //Face where the rat is currently located on the screen
		horizontalInput = Input.GetAxisRaw("Horizontal")*(turnSpeedParameters[0]*turnSpeedParameters[1])*Time.deltaTime;
		transform.Rotate(Vector3.up*horizontalInput); //Rotate rat when moving sideways
	}

	public void AllowMovement(bool allowToMove){ //Suspend input For cutscenes or cooldowns
		freeToMove=allowToMove;
	}
}
