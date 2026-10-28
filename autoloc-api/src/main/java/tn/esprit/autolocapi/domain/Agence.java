package tn.esprit.autolocapi.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class Agence {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idAgence;

    private String nom;
    private String ville;
    private String adresse;
    private String telephone;

    @OneToMany(mappedBy = "agence")
    @com.fasterxml.jackson.annotation.JsonIgnore
    private List<Vehicule> vehicules;

    @OneToMany(mappedBy = "agence")
    @com.fasterxml.jackson.annotation.JsonIgnore
    private List<Employe> employes;
}
