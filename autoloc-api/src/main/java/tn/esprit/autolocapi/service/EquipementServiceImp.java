package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Equipement;
import tn.esprit.autolocapi.repository.EquipementRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class EquipementServiceImp implements IEquipementService {

    private final EquipementRepository equipementRepository;

    @Override
    public Equipement ajouterEquipement(Equipement equipement) {

        return equipementRepository.save(equipement);
    }

    @Override
    public Equipement modifierEquipement(Equipement equipement) {

        return equipementRepository.save(equipement);
    }

    @Override
    public Equipement getEquipementById(Long id) {

        return equipementRepository.findById(id).orElse(null);
    }

    @Override
    public List<Equipement> getAllEquipement() {

        return equipementRepository.findAll();
    }

    @Override
    public Equipement supprimerEquipementById(Long id) {
        Equipement equipement = getEquipementById(id);
        if (equipement != null) {
            equipementRepository.deleteById(id);
        }
        return equipement;
    }
}
