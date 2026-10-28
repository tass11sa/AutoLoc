package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Reservation;

import java.util.List;

public interface IReservationService {
    public Reservation ajouterReservation(Reservation reservation);
    public Reservation modifierReservation(Reservation reservation);
    public Reservation getReservationById(Long id);
    public List<Reservation> getAllReservation();
    public Reservation supprimerReservationById(Long id);
}
