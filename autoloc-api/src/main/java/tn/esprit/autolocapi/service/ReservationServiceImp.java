package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Reservation;
import tn.esprit.autolocapi.repository.ReservationRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class ReservationServiceImp implements IReservationService {

    private final ReservationRepository reservationRepository;

    @Override
    public Reservation ajouterReservation(Reservation reservation) {

        return reservationRepository.save(reservation);
    }

    @Override
    public Reservation modifierReservation(Reservation reservation) {

        return reservationRepository.save(reservation);
    }

    @Override
    public Reservation getReservationById(Long id) {

        return reservationRepository.findById(id).orElse(null);
    }

    @Override
    public List<Reservation> getAllReservation() {

        return reservationRepository.findAll();
    }

    @Override
    public Reservation supprimerReservationById(Long id) {
        Reservation reservation = getReservationById(id);
        if (reservation != null) {
            reservationRepository.deleteById(id);
        }
        return reservation;
    }
}
