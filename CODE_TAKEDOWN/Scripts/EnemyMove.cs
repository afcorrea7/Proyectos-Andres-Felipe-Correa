using UnityEngine;
using System.Collections;

public class EnemyMove : MonoBehaviour {
	public float wayMoveSpeed = 5f;		// enemy move speed
	public GameObject[] myWaypoints;	// all waypoints
	private int myWaypointId = 0;		// used as index for My_Waypoints	

    Animator anim;

    private void Start()
    {
        anim = GetComponent<Animator>();
    }

    void EnemyMovement() {
		// if there isn't anything in My_Waypoints
		if(myWaypoints.Length != 0) {
			// if the enemy is close enough to waypoint, make it's new target the next waypoint
			if(Vector3.Distance(myWaypoints[myWaypointId].transform.position, transform.position) <= 0) {
				myWaypointId++;
			}
			
			if(myWaypointId >= myWaypoints.Length) {
				myWaypointId = 0;
			}
			
			// move towards waypoint
			transform.position = Vector3.MoveTowards(transform.position, myWaypoints[myWaypointId].transform.position, wayMoveSpeed * Time.deltaTime);
            
		}
	}
	
	// Update is called once per frame
	void Update () {
		EnemyMovement();
        anim.SetBool("IsWalking", true);
	}
}