using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyChaser2D : MonoBehaviour
{
    public Transform target;
    public GameObject attackHitBox;
    public float enemyRange = 8f;
    public float moveSpeed = 3f;
    public float enemyAttackRange = 0.8f;

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
        //check distance to player
        float distToPlayer = Vector2.Distance(transform.position, target.position);
        Debug.LogWarning("distToPlayer: " + distToPlayer);

        if (distToPlayer < enemyRange)
        {
            //Chase the player
            ChasePlayer();
        }
        else if (distToPlayer > enemyRange)
        {
            //stop chasing player
            StopChase();
            anim.SetBool("IsWalking", false);
        }

        if(distToPlayer < enemyAttackRange && !isPunching)
        {
            isPunching = true;
            anim.SetTrigger("SetPunch");
            StartCoroutine(DoAttack());
        }

    }

    IEnumerator DoAttack()
    {
        //activate hitbox, then deactivate it
        attackHitBox.SetActive(true);
        yield return new WaitForSeconds(0.3f);
        attackHitBox.SetActive(false);
        //Cooldown between attacks
        yield return new WaitForSeconds(0.8f);
        //Allow the player to attack again
        isPunching = false;
    }

    void ChasePlayer()
    {
        transform.position = Vector2.MoveTowards(transform.position, target.position, moveSpeed *Time.deltaTime);
        anim.SetBool("IsWalking", true);
        if (transform.position.x < target.position.x)
        {
            //enemy is to the Player's left so enemy is facing right
            transform.localEulerAngles = new Vector3(0, 0, 0);
        }

        if(transform.position.x > target.position.x)
        {
            //enemy is to the Player's right so enemy is facing left
            transform.localEulerAngles = new Vector3(0, 180, 0);
        }
    }

    void StopChase()
    {
        anim.SetBool("IsWalking", false);
        rb.velocity = Vector2.zero;
    }
}
