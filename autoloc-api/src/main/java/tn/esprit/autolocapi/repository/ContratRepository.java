package tn.esprit.autolocapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import tn.esprit.autolocapi.domain.Contrat;

@Repository
public interface ContratRepository extends JpaRepository<Contrat, Long> {
}
