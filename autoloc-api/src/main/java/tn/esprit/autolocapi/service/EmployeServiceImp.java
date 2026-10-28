package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Employe;
import tn.esprit.autolocapi.repository.EmployeRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class EmployeServiceImp implements IEmployeService {

    private final EmployeRepository employeRepository;

    @Override
    public Employe ajouterEmploye(Employe employe) {

        return employeRepository.save(employe);
    }

    @Override
    public Employe modifierEmploye(Employe employe) {

        return employeRepository.save(employe);
    }

    @Override
    public Employe getEmployeById(Long id) {

        return employeRepository.findById(id).orElse(null);
    }

    @Override
    public List<Employe> getAllEmploye() {

        return employeRepository.findAll();
    }

    @Override
    public Employe supprimerEmployeById(Long id) {
        Employe employe = getEmployeById(id);
        if (employe != null) {
            employeRepository.deleteById(id);
        }
        return employe;
    }
}
