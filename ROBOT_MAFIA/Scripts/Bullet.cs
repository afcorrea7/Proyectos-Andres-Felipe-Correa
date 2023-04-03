using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet : MonoBehaviour
{
    [SerializeField]
    GameObject enemParent;
    [SerializeField]
    GameObject playerObject;
    [SerializeField]
    GameObject gun;

    [SerializeField]
    GameObject uiScore;

    private EnemyLayer enemLayer;
    private Controller playerController;
    private Aim aimScript;
    private Score uiScript;
    private Vector3 firingPoint;
    private BoxCollider thisColl;
    

    [SerializeField]
    float destroyTime;
    [SerializeField]
    float projectileSpeed; //Bullet speed
    [SerializeField]
    float speedIncrease=0.15f;
    [SerializeField]
    float pitchIncrease=0.25f;
    [SerializeField]
    private float maxBulletDistance;
    [SerializeField]
    private Rigidbody thisRigid;
    [SerializeField]
    private TrailRenderer bulletTrail;
    [SerializeField]
    private AudioSource thisAudioSource;

    Vector3 lastVelocity; //Used for .magnitude when calculating Vector3.Reflect()
    private float speedAfterBounce=1; //Increasing amount with every bounce, makes the bullet faster after a bounce
    private float currentPitch=0.5f;
    [HideInInspector]
    public int bounceCount; //counts number of bounces so far.
    private int bounceScore; //For adding bounces to Score UI

    void Awake() //Awake siempre es ejecutado antes de Start
    {
        enemParent = GameObject.Find("Enemigos");
        playerObject = GameObject.Find("Player");
        gun = GameObject.Find("Gun");
        uiScore = GameObject.Find("Score");

        aimScript = gun.GetComponent<Aim>();
        playerController = playerObject.GetComponent<Controller>();
        enemLayer = enemParent.GetComponent<EnemyLayer>();
        uiScript = uiScore.GetComponent<Score>();

        thisRigid = GetComponent<Rigidbody>();
        thisColl = GetComponent<BoxCollider>();
        bulletTrail = GetComponent<TrailRenderer>();
        thisAudioSource = GetComponent<AudioSource>();
        firingPoint = transform.position;

    }

    void Start() 
    {   
        playerController.AllowMovement(false);

        MoveBullet(); //ideally, the player can only shoot one bullet at a time, after the previous has stopped
        enemLayer.toggleTrigger(false); //tell enemy hitbox to turn off trigger so the bullet collides with them
        //Before the first bounce bullet can't go through enemies, after first bounce it can.

        Physics.IgnoreLayerCollision(3, 3, true); // IgnorelayerCollision(a layer, another layer, bool ignore);
    }
    
    void Update()
    {
        if(Vector3.Distance(firingPoint, transform.position)> maxBulletDistance){ // if the bullet is far away from the max distance, the bullet gets destroyed
            Destroy(this.gameObject);
            playerController.AllowMovement(true);
        }
        lastVelocity = thisRigid.velocity; //update bullet direction

        Destroy(this.gameObject, destroyTime); //Destroy bullet after certain time has passed

        BounceColor();
    }

    void MoveBullet(){       
            thisRigid.AddForce(transform.forward*projectileSpeed*Time.deltaTime, ForceMode.Impulse); //Add force forward after spawning bullet
            //transform.Translate(Vector3.forward*projectileSpeed*Time.deltaTime); //move the bullet x distance
    }

    private void OnCollisionEnter(Collision other) {
        if(other.collider.tag!="Mirror" || bounceCount==aimScript.numReflections){ //If it collides with a wall or an Enemy before its first bounce the bullet stops
            projectileSpeed=0;
            thisRigid.isKinematic=true;
            if(other.collider.tag=="Enemy" || other.collider.tag=="Player"){
                Destroy(this.gameObject, 1); //If hit an enemy and stopped, destroy
            }
            enemLayer.toggleTrigger(false);

            playerController.AllowMovement(true); //The bullet has stopped, player can shoot or move again
        }
 
        if(other.collider.tag=="Mirror" && bounceCount<aimScript.numReflections){ //Reflect if bullet collides with a mirror or it hasn't reached max bounces
            ReflectBullet(other.contacts[0].normal); //Get the normal vector of that Mirror's face
        } 
     
    }

    private void ReflectBullet(Vector3 theNormal){
        Debug.Log("Attempt");

        //Audio clip increases in pitch after everybounce
        currentPitch += bounceCount*pitchIncrease;
        thisAudioSource.pitch = currentPitch;
        thisAudioSource.Play();

        speedAfterBounce += speedIncrease; //Increase bullet speed
        var newSpeed = lastVelocity.magnitude*speedAfterBounce;
        var direction = Vector3.Reflect(lastVelocity.normalized, theNormal);
        thisRigid.velocity = direction*newSpeed;

        bounceCount++;
        enemLayer.toggleTrigger(true); //Tell enemies hitbox to turn into triggers so the bullet goes through

        //For scoring
        bounceScore += bounceCount*100;
        Debug.Log("bounceScore: "+bounceScore);
        StartCoroutine(uiScript.MultiplierSprite(bounceCount));
        StartCoroutine(uiScript.AddBounceScore(bounceScore));
        
        //transform.Translate(Vector3.Reflect(this.gameObject.transform.position, theNormal));
    }


    private void BounceColor(){
        if(bounceCount==1){
            bulletTrail.startColor = Color.yellow;
            Debug.Log("color1");
        }else if(bounceCount==2){
            bulletTrail.startColor = Color.magenta;
            Debug.Log("color2");
        }else if(bounceCount==3 || bounceCount>=aimScript.numReflections){
            bulletTrail.startColor = Color.red;
            Debug.Log("color3");
        }
    }
}
