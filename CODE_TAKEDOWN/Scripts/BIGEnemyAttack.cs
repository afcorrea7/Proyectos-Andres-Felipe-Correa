using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BIGEnemyAttack : MonoBehaviour
{
    public Transform target;
    public GameObject attackHitBox;
    public float enemyRange = 1.5f;

    private bool isPunching = false;

    Rigidbody2D rb;
    Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();

        attackHitBox.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        float distToPlayer = Vector2.Distance(transform.position, target.position);

        if (distToPlayer < enemyRange && !isPunching)
        {
            isPunching = true;
            anim.SetTrigger("SetPunch");
            StartCoroutine(DoAttack());
        }

        if (transform.position.x > target.position.x)
        {
            //enemy is to the Player's left so enemy is facing right
            transform.localEulerAngles = new Vector3(0, 0, 0);
        }

        if (transform.position.x < target.position.x)
        {
            //enemy is to the Player's right so enemy is facing left
            transform.localEulerAngles = new Vector3(0, 180, 0);
        }
    }

    IEnumerator DoAttack()
    {
        //Wait before attacking
        yield return new WaitForSeconds(0.8f);
        //activate hitbox, then deactivate it
        attackHitBox.SetActive(true);
        yield return new WaitForSeconds(0.4f);
        attackHitBox.SetActive(false);
        //Cooldown between attacks
        yield return new WaitForSeconds(1f);
        //Allow the player to attack again
        isPunching = false;
    }
}
