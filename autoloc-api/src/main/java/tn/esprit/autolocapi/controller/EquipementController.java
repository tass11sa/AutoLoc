package tn.esprit.autolocapi.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import tn.esprit.autolocapi.domain.Equipement;
import tn.esprit.autolocapi.service.IEquipementService;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/equipements")
public class EquipementController {

    private final IEquipementService equipementService;

    @PostMapping("/ajouter")
    public Equipement ajouterEquipement(@RequestBody Equipement equipement) {
        return equipementService.ajouterEquipement(equipement);
    }

    @PutMapping("/modifier")
    public Equipement modifierEquipement(@RequestBody Equipement equipement) {
        return equipementService.modifierEquipement(equipement);
    }

    @GetMapping("/{id}")
    public Equipement getEquipementById(@PathVariable Long id) {
        return equipementService.getEquipementById(id);
    }

    @GetMapping("/all")
    public List<Equipement> getAllEquipements() {
        return equipementService.getAllEquipement();
    }

    @DeleteMapping("/supprimer/{id}")
    public Equipement supprimerEquipementById(@PathVariable Long id) {
        return equipementService.supprimerEquipementById(id);
    }
}
