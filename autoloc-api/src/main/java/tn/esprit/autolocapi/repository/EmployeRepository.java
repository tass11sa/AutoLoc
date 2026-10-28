package tn.esprit.autolocapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import tn.esprit.autolocapi.domain.Employe;

@Repository
public interface EmployeRepository extends JpaRepository<Employe, Long> {
}
