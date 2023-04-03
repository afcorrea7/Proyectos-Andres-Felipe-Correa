using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyHealth : MonoBehaviour
{
    //Vertical boundaries
    static Vector2 LimitsY = new Vector2(-5f, -1.59f);
    //Horizontal boundaries
    static Vector2 LimitsX = new Vector2(-9.42f, 78.10f);

    SpriteRenderer sr;
    Rigidbody2D rb;
    Animator anim;
    CapsuleCollider2D coll;
    AudioSource aud; 


    public int health = 5;
    public AudioClip enemyHurtSFX;
    public AudioClip enemyBurnSFX;
    public GameObject explosion;

    int enemyPunchLayer;
    int playerPunchLayer;

    // Start is called before the first frame update
    void Start()
    {
        sr = GetComponent<SpriteRenderer>();
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        coll = GetComponent<CapsuleCollider2D>();
        aud = GetComponent<AudioSource>();

        enemyPunchLayer = LayerMask.NameToLayer("EnemyPunchLayer");
        playerPunchLayer = LayerMask.NameToLayer("PunchLayer");
    }

    // Update is called once per frame
    void Update()
    {

        Physics2D.IgnoreLayerCollision(enemyPunchLayer, playerPunchLayer);
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.tag == "Punch")
        {
            anim.SetTrigger("SetHurt");
            aud.PlayOneShot(enemyHurtSFX);
            health -= 1;
            Debug.Log("Collision detected");
        }

        if (other.gameObject.tag == "Fireball")
        {
            anim.SetTrigger("SetHurt");
            aud.PlayOneShot(enemyBurnSFX);
            health -= 5;
        }

        if (health <= 0)
        {
            Instantiate(explosion, transform.position, transform.rotation);
            Destroy(gameObject, 0.2f);
            Debug.Log("Enemy dead");
        }
    }

    private void FixedUpdate()
    {
        //Set the map boundaries
        transform.position = new Vector3(Mathf.Clamp(transform.position.x, LimitsX.x, LimitsX.y),
            Mathf.Clamp(transform.position.y, LimitsY.x, LimitsY.y), //Mathf.Clamp sets the Y pos limits
            transform.position.z);
    }
}
