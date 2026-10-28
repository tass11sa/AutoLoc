package tn.esprit.autolocapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import tn.esprit.autolocapi.domain.Paiement;

@Repository
public interface PaiementRepository extends JpaRepository<Paiement, Long> {
}
