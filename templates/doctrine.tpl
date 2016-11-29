<?php

namespace myBundle

use Doctrine\ORM\Mapping as ORM;

/**
 *
 * @ORM\Table(name="{{ table_name }}")
 * @ORM\Entity
 */
class {{ entity_name }}
{
    /**
     * @ORM\Column(type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;
    {# -#}
    {% for field in fields %}
    /**
    * @ORM\Column(type="{{ field.type }}")
    **/
    private ${{ field.variable_name }}
    {% endfor %}
    {# -#}
    /**
     * Set id
     **/
    public function setId($id)
    {
        $this->id = $id;
    }

    /**
     * Get id
     **/
    public function getId()
    {
        return $this->id;
    }
    {# -#}
    {% for field in fields %}
    /**
     * Set {{ field.name }}
     **/
    function set{{ field.method_name}}(${{field.variable_name}}){
        $this->{{field.variable_name}} = ${{field.variable_name}};
    }

    /**
     * Get {{ field.name }}
     **/
    function get{{ field.method_name}}(){
        return $this->{{field.variable_name}};
    }    
    {% endfor %}
}

?>