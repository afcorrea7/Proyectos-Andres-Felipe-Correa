using UnityEngine;
using System.Collections;

public class Controller : MonoBehaviour {
	
	// public variables
	public float speed=4;
	public float minimumHold=0.7f; //Minimun time for the fire button to be pressed to be considered "Held"
	public PlayerGun pGun;
	public Aim pAim;
	//private variables
	float horizontalInput;
    float verticalInput;
	bool freeToMove=true; //Start being able to move
   	private Rigidbody player;

	//For checking button held down
	private float firePressedTime;
	private bool fireHeld = false;
	
	// Use this for initialization
	void Start () {
		//pGun=GetComponent<PlayerGun>();
		player=GetComponent<Rigidbody>();
	}
	
	// Update is called once per frame
	void Update () {
		if(freeToMove){
			PlayerMovement();
			PlayerRotation();

			PlayerInput();
		}
	}

	void PlayerMovement(){
		horizontalInput=Input.GetAxis("Horizontal");
    	verticalInput=Input.GetAxis("Vertical");

		Vector3 movement=new Vector3(horizontalInput,0,verticalInput);
        transform.Translate(movement*speed*Time.deltaTime, Space.World);
	}

	void PlayerRotation(){ //Face where the mouse is currently located on the screen
		RaycastHit hit;
		Ray ray= Camera.main.ScreenPointToRay(Input.mousePosition);

		if(Physics.Raycast(ray,out hit)){
			transform.LookAt(new Vector3(hit.point.x,transform.position.y,hit.point.z));
		}
	}

	void PlayerInput(){
		if (Input.GetButtonDown("Fire1")) {
        	// Player has pressed the Space key. We don't know if they'll release or hold it, so keep track of when they started holding it.
        	firePressedTime = Time.timeSinceLevelLoad;
        	fireHeld = false;
   		 
		}else if(Input.GetButtonUp("Fire1")){
        	if (!fireHeld) {
            	// Player has released the space key without holding it.
				Debug.Log("Player DID NOT HOLD");
        	}

			if(fireHeld){
				Debug.Log("Player HELD and RELEASED");
				pAim.RayoGuia(false); //Deactive aim ray
				pGun.Shoot(); //And shoot
			}
		}
		
    	if (Input.GetButton("Fire1")) {
        	if (Time.timeSinceLevelLoad - firePressedTime > minimumHold) {
           		// Player has held the Space key for miminumHold seconds. Consider it "held"
				Debug.Log("Player is HOLDING");
            	fireHeld = true;
				pAim.RayoGuia(true); //Activate aim ray
           	}
    	}
	}

	public void AllowMovement(bool free){
		freeToMove=free;
	}

	public void Bruh(){
		Debug.Log("Bruh");
	}
}
