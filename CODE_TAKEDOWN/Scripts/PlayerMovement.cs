using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerMovement : MonoBehaviour
{
    public string levelToLoad;
    //Vertical boundaries
    static Vector2 LimitsY = new Vector2(-5f, -1.59f);
    //Horizontal boundaries
    static Vector2 LimitsX = new Vector2(-9.42f, 78.10f);

    public float moveSpeed = 3f;
    public float coolDown = 5f;
    public int playerHealth = 10;

    //The game object's child is going to be the punch hitbox
    public GameObject attackHitBox;
    public GameObject fireBallToRight, fireBallToLeft;
    public AudioClip playerHurtSFX;

    private float nextFire = 5f;
    private bool IsPunching = false;
    private bool facingRight;

    int enemyPunchLayer;
    int playerPunchLayer;

    //Establish Game object's components
    SpriteRenderer sr;
    Rigidbody2D rb;
    Animator anim;
    AudioSource aud;

    Vector2 movement;
    Vector2 fireBallPos;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        sr = GetComponent<SpriteRenderer>();
        aud = GetComponent<AudioSource>();

        attackHitBox.SetActive(false);

        enemyPunchLayer = LayerMask.NameToLayer("EnemyPunchLayer");
        playerPunchLayer = LayerMask.NameToLayer("PunchLayer");
    }

    // For player Input
    void Update()
    {
        //Detect player input for x and y axis
        movement.x = Input.GetAxisRaw("Horizontal");
        movement.y = Input.GetAxisRaw("Vertical");

        //Play walking animation if moving
        anim.SetBool("IsWalking", movement.magnitude != 0);

        //Flip the sprite if facing left
        if (movement.x < 0)
        {
            transform.localEulerAngles = new Vector3(0, 180, 0);
            facingRight = false;
        }
        if (movement.x > 0)
        {
            facingRight = true;
            transform.localEulerAngles = new Vector3(0, 0, 0);
        }

        //Player attack
        if (Input.GetButtonDown("Fire1") && !IsPunching)
        {
            //Turn off the ability to attack so the player can't keep pressing the button and the hitbox doesn't stay active all the time
            IsPunching = true;
            anim.SetTrigger("SetPunch");
            //Start a coroutine to set a cooldown
            StartCoroutine(DoAttack());
        }

        if(Input.GetButtonDown("Fire2") && Time.time > nextFire)
        {
            nextFire = Time.time + coolDown;
            StartCoroutine (Fireball ());
        }

        if (playerHealth <= 0)
        {
            Destroy(gameObject, 0.5f);
            Debug.LogWarning("F in the chat");
        }

        if(playerHealth <= 0)
        {
            LoadLevel();
        }

        Physics2D.IgnoreLayerCollision(enemyPunchLayer, playerPunchLayer);
    }

    IEnumerator DoAttack()
    {
        //activate hitbox, then deactivate it
        attackHitBox.SetActive(true);
        yield return new WaitForSeconds(0.5f);
        attackHitBox.SetActive(false);
        //Allow the player to attack again
        IsPunching = false;
    }

    IEnumerator Fireball()
    {
        anim.SetTrigger("SetFirePerk");
        yield return new WaitForSeconds(1f);
        fireBallPos = transform.position;
        if (facingRight == true)
        {
            fireBallPos += new Vector2(+1f, 0.2f);
            Instantiate (fireBallToRight, fireBallPos, Quaternion.identity);
        }

        if(facingRight == false)
        {
            fireBallPos += new Vector2(-1f, 0.2f);
            Instantiate(fireBallToLeft, fireBallPos, Quaternion.identity);
        }
    }

    //For movement
    private void FixedUpdate()
    {
        //Current player movement
        rb.MovePosition(rb.position + movement * moveSpeed * Time.fixedDeltaTime);

        //Set the map boundaries
        transform.position = new Vector3(Mathf.Clamp(transform.position.x, LimitsX.x, LimitsX.y),
            Mathf.Clamp(transform.position.y, LimitsY.x, LimitsY.y), //Mathf.Clamp sets the Y pos limits
            transform.position.z);
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.tag == "EnemyPunch")
        {
            anim.SetTrigger("SetHurt");
            aud.PlayOneShot(playerHurtSFX);
            playerHealth -= 1;
            HealthBarScript.health -= 1;
        }

        if(other.gameObject.tag == "BIGPunch")
        {
            anim.SetTrigger("SetHurt");
            aud.PlayOneShot(playerHurtSFX);
            playerHealth -= 3;
            HealthBarScript.health -= 3;
        }

        if(other.gameObject.tag == "VictoryBat")
        {
            movement = Vector2.zero;
        }
    }

    void LoadLevel()
    {
        SceneManager.LoadScene(levelToLoad);
    }
}
