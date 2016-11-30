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

{% for field in fields %}
    {% if not field.relationship %}
    /**
     * @ORM\Column(type="{{ field.type }}"{% for extra in field.extras %}, {{ extra }}{% endfor %})
     **/
    private ${{ field.variable_name }};

    {% else %}
        {% if field.relationship.type == "OneToMany" %}
    /**
     * @OneToMany(targetEntity="{{ field.relationship.targetEntity }}", mappedBy="{{ field.relationship.mappedBy }}")
     */
    private ${{ field.variable_name }};

        {% elif field.relationship.type == "ManyToMany" %}
    /**
     * @ORM\ManyToMany(targetEntity="{{ field.relationship.targetEntity }}", inversedBy="{{field.relationship.inversedBy|pluralize}}")
     * @ORM\JoinTable(name="{{field.relationship.inversedBy|pluralize}}_{{field.relationship.source|pluralize}}")
     */   
    private ${{ field.variable_name }};  

        {% endif %}
    {% endif %}
{% endfor %}
    /**
     * Constructor
     **/
    public function __construct()
    {
{% for field in fields %}
    {% if field.relationship %}
        {% if field.relationship.type == "ManyToMany" %}
        $this->{{field.variable_name}} = new \Doctrine\Common\Collections\ArrayCollection();
        {% endif %}
    {% endif %}
{% endfor %}
    }

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

{% for field in fields %}
    {% if  not field.relationship %}
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

    {% else %}
        {% if field.relationship.type == "OneToMany" %}

    /**
     * Set {{ field.name }}
     **/
    function set{{ field.method_name}}({{field.relationship.targetEntity}} ${{field.variable_name}}){
        $this->{{field.variable_name}} = ${{field.variable_name}};
    }
    
    /**
     * Get {{ field.name }}
     **/
    function get{{ field.method_name}}(){
        return $this->{{field.variable_name}};
    }

        {% elif field.relationship.type == "ManyToMany" %}
    /**
     * Add {{ field.name }}
     **/
    function add{{ field.method_name}}({{field.relationship.targetEntity}} ${{field.variable_name}}){
        $this->{{field.variable_name}} = ${{field.variable_name}};
    }

    /**
     * Get {{ field.name }}
     **/
    function get{{ field.method_name}}(){
        return $this->{{field.variable_name}};
    }

        {% endif %}
    {% endif %}
{% endfor %}
}

?>