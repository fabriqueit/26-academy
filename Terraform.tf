// TERAFORM FILE FOR E-SANTE project part 3
// Author : Philippe Colson
// Tutor : Ivan Beauté


// CONFIG AND PLUG-IN PART ***********************

// Configure the Google Cloud provider with ID file for credential
provider "google" {
  credentials = "${file("26A_E-Sante-762d351e2206.json")}"
  project     = "bustling-dynamo-216319"
  region      = "europe-west1"
  zone        = "europe-west1-b"
}

// Terraform plugin for creating random ids
resource "random_id" "instance_id" {
 byte_length = 8
}


// CREATE INSTANCE PART *****************************

// A single Google Cloud Engine instance
resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance-${random_id.instance_id.hex}"
  machine_type = "n1-standard-2"
  // Necessary for local VM on the same local network
  zone         = "europe-west1-b"

  // Add a public ssh key to the Google Cloud Engine instance to access and manage it.
  metadata {
   sshKeys = "pcolson:${file("26A_E-Sante.pub")}"
  }
  // Ubuntu 16.04 LTS operating system as required with persistent 30 GB drive
  boot_disk {
    initialize_params {
      image = "ubuntu-1604-lts"
      type  = "pd-standard"
      size  = "30"
    }
  }

// Make sure docker is installed on all new instances for later steps
 metadata_startup_script = "sudo apt update; sudo apt install -y docker.io; sudo usermod -aG docker $USER"

// Network config by default
  network_interface {
    // A default network is created for all GCP projects
    network       = "default"
    access_config = {
    // Include this section to give the VM an external ip address
    }
  }
}
// authorize HTTP, HTTPS traffic through firewall and ICMP for monitoring
resource "google_compute_firewall" "default" {
  name    = "allow-http-https"
  network = "${google_compute_network.default.name}"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080", "443", "1000-2000"]
  }

  source_tags = ["web"]
}

resource "google_compute_network" "default" {
  name = "my-network"
}


// OUTPUT PART *************************************

// A variable for extracting the external ip of the instance
output "ip" {
 value = "${google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip}"
}