package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Client;
import tn.esprit.autolocapi.repository.ClientRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class ClientServiceImp implements IClientService {

    private final ClientRepository clientRepository;

    @Override
    public Client ajouterClient(Client client) {
        return clientRepository.save(client);
    }

    @Override
    public Client modifierClient(Client client) {
        return clientRepository.save(client);
    }

    @Override
    public Client getClientById(Long id) {

        return clientRepository.findById(id).orElse(null);
    }

    @Override
    public List<Client> getAllClient() {

        return clientRepository.findAll();
    }

    @Override
    public Client supprimerClientById(Long id) {
        Client client = getClientById(id);
        if (client != null) {
            clientRepository.deleteById(id);
        }
        return client;
    }
}
