package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Maintenance;

import java.util.List;

public interface IMaintenanceService {
    public Maintenance ajouterMaintenance(Maintenance maintenance);
    public Maintenance modifierMaintenance(Maintenance maintenance);
    public Maintenance getMaintenanceById(Long id);
    public List<Maintenance> getAllMaintenance();
    public Maintenance supprimerMaintenanceById(Long id);
}
