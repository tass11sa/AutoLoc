package tn.esprit.autolocapi.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import tn.esprit.autolocapi.domain.Agence;
import tn.esprit.autolocapi.service.IAgenceService;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/agences")
public class AgenceController {

    private final IAgenceService agenceService;

    @PostMapping("/ajouter")
    public Agence ajouterAgence(@RequestBody Agence agence) {

        return agenceService.ajouterAgence(agence);
    }

    @PutMapping("/modifier")
    public Agence modifierAgence(@RequestBody Agence agence) {

        return agenceService.modifierAgence(agence);
    }

    @GetMapping("/{id}")
    public Agence getAgenceById(@PathVariable Long id) {

        return agenceService.getAgenceById(id);
    }

    @GetMapping("/all")
    public List<Agence> getAllAgences() {
        return agenceService.getAllAgence();
    }

    @DeleteMapping("/supprimer/{id}")
    public Agence supprimerAgenceById(@PathVariable Long id) {
        return agenceService.supprimerAgenceById(id);
    }
}
