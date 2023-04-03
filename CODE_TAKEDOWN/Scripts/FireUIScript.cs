using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FireUIScript : MonoBehaviour
{
    public Image firePerk;
    public float coolDown = 5f;

    private bool isCoolDown;
    private bool firstCoolDown = false;
    // Start is called before the first frame update
    // Update is called once per frame
    void Update()
    {
        if (!firstCoolDown)
        {
            firePerk.fillAmount += 1 / coolDown * Time.deltaTime;

            if (firePerk.fillAmount >= 1)
            {
                firstCoolDown = true;
            }
        }

        if (Input.GetButtonDown("Fire2") && firstCoolDown && firePerk.fillAmount >= 1)
        {
            isCoolDown = true;
            firePerk.fillAmount = 0;

        }
        if (isCoolDown)
        {
            firePerk.fillAmount += 1 / coolDown * Time.deltaTime;

            if(firePerk.fillAmount >= 1)
            {
                isCoolDown = false;
            }
        }
    }
}
